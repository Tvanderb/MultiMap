import click
import os
import subprocess

class prefix:
    OK = "[\u001b[32;1m*\u001b[0m]"
    ERR = "[\u001b[31m-\u001b[0m]"
    WARN = "[\u001b[33;1m#\u001b[0m]"
    MSG = "[\u001b[35m*\u001b[0m]"
    UNK = "[\u001b[36;1m?\u001b[0m]"

class log:
    def ok(msg):
        print(prefix.OK, msg)
    def err(msg):
        print(prefix.ERR + "\u001b[31m", "\u001b[4m", msg + " \u001b[0m")
    def warn(msg):
        print(prefix.WARN + "\u001b[33m", msg, "\u001b[0m")
    def msg(msg):
        print(prefix.MSG, msg)
    def unk(msg):
        print(prefix.UNK, msg)


@click.command("MMap", )
@click.argument("hosts", required=True)
@click.option("--no-save", "-ns", is_flag=True, help="Prevents MultiMap from saving output to files.")
@click.option("--output-here", "-oh", is_flag=True, help="Create output files in your current directory.")
@click.option("--folder-name", "-fn", type=str, help="Choose the name of the folder that will contain the output files.")
@click.option("--yes", "-y", is_flag=True, help="Skip the y/n prompt at the beginning.")
@click.option("-Pn", is_flag=True, help="Run ping scans instead of normal NMap scans.")
def main(hosts, no_save, output_here, folder_name, yes, pn):
    hosts = hosts.split(",")
    path = os.getcwd()

    if not yes:
        if not click.confirm("You are about to execute " + str(len(hosts)) + " nmap command(s) in " + path + ". Do you want to continue?"):
            return

    if not output_here:
        name = "mmap"
        if folder_name is not None:
            name = folder_name
        path = path + "\\" + name
        try:
            os.mkdir(path)
        except FileExistsError:
            1 == 1

    for host in hosts:
        log.ok("Running NMap scan against " + host + "...")
        file = open(path + "\\" + host + ".txt", "a")
        command = "nmap -v -A " + host
        if pn:
            command = "nmap -Pn " + host
        subprocess.Popen(command, stdout=file, stdin=open(os.devnull, "w"))
        file.close()

    log.warn("The files created by MultiMap will be used by the NMap processes until the scan(s) are complete. I can't really find away around that, sorry for the inconvenience.")


if __name__ == "__main__":
    main()
