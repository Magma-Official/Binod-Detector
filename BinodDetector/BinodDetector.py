import os
import pyfiglet

#************************************************

print("\n\n")
result = pyfiglet.figlet_format("Binod  Detector")
print(result)

print("Made by :- Magma Official")
print("Visit :- www.codingindia.ml")
print("\n")
print("[ It Will Detect word Binod in all txt files present in your Current Directory ]")

print("-----------------------------------------------------------------------------------")
#****************************************************************************************************

print("\n")

print("*** Detecting Binod.....")
print(".")
print(".")
print(".")
print(".")
print(".")
print("\n")


def isBinod(filename):
    with open(filename, "r") as f:
        fileContent = f.read()

    # Detecting all forms of Binod like BiNod, binOd etc.
    if "binod" in fileContent.lower():
         return True
    else:
         return False

if __name__ == "__main__":

    #Listing the content in this folder
    dir_contents = os.listdir()

    nBinod = 0
    #for each text file; run isBinod for them
    for item in dir_contents:
        if item.endswith('txt'):
            print(f"Detecting Binod in - {item}")
            flag = isBinod(item)
            if (flag):
                print(f"#*****************# Binod Found in - {item} !!!!!!!!!!!!!!", end="\n\n")
                nBinod += 1
            else:
                print(f"xxxxx-- Binod Not Found in - {item} --xxxxx", end="\n\n")

    print("\n")
    print(f"***********### --- Binod Ditector Summery --- ###***********", end="\n\n\n")
    if(nBinod == 0):
        print("#### Binod Not Detected in Any File ! ####", end="\n\n\n\n")
    else:
        print("Congratulation !!! BINOD Detected in Your Files...", end="\n\n")
        print(f"{nBinod} - Files Found 'Binod' Hidden into them...", end="\n\n\n\n")
