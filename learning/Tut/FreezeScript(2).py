import time
import subprocess

def main():
    x = open("setup.py", "w")
    nameTo = str(input("Please input the name of the file to be: "))
    nameFrom = str(input("Please input the name of the file: "))
    version = str(input("Please input version number: "))
    k = str('from cx_Freeze import setup, Executable\nsetup(name="'+nameTo+'", version="'+version+'", executables = [Executable("' + nameFrom+'")])')
    x.write(k)
    x.close()
    command = "C:\Python34\python setup.py build"
    time.sleep(1)
    subprocess.call(r'C:\Python34\python setup.py build', shell=True)
    print(subprocess.call("C:\Python34\python setup.py build"))

if __name__ == "__main__":
    main()
