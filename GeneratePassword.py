import os, random, string

class GeneratePassword:

    def __init__(self):
        self.delim = "^&%*!£()_-+='@#~}{][/?><|\¬`:;.,"
    
    def english_dictionary(self):
        words = []
        with open("dictionary.txt", "r") as d:
            for i in d:
                w = i.strip('\n')
                words.append(w)
        d.close()

        return words
    
    def password(self, words, delimiter):
        password, dictionary = "", self.english_dictionary()
        
        for i in range(0, words):
            if i%2==0:
                n = random.SystemRandom().randint(0, len(dictionary)-1)
                password += dictionary[n]+str(delimiter)
            else:
               n = random.SystemRandom().randint(0, len(dictionary)-1)
               password += dictionary[n]+str(delimiter[::-1]) 

        return password[0:len(password)-len(delimiter)]

    def sys_rand_char(x):
        return random.SystemRandom().randint(0, len(x)-1)
    
    def main(self):
        print("P-H-A-N-T-O-M\nPassword Generator")
        select = str(input("1 - Level based complexity\n2 - self selected complexity\nSelection: "))        
        if select == "1":
            complexityLevel = str(input("1 - Basic\n2 - Medium\n3 - Extreme\n4 - Phantom\nSelection: "))
            if complexityLevel == "1":
                w, dl = random.SystemRandom().randint(4, 8), self.sys_rand_char(self.delim)
                print(self.password(w, self.delim[dl]))
            elif complexityLevel == "2":
                w, dl = random.SystemRandom().randint(8, 12), self.sys_rand_char(self.delim)
                print(self.password(w, self.delim[dl]))
            elif complexityLevel == "3":
                w, dl = random.SystemRandom().randint(12, 16), self.sys_rand_char(self.delim)
                print(self.password(w, self.delim[dl]))
            elif complexityLevel == "4":
                w, dl = random.SystemRandom().randint(16, 30), self.sys_rand_char(self.delim)
                asciiChar = self.sys_rand_char(string.ascii_letters)
                digits = self.sys_rand_char(string.digits)
                delimiter = self.delim[dl] + string.ascii_letters[asciiChar] + string.digits[digits]
                print(self.password(w, delimiter))
        if select == "2":
            w, dl = int(input("Enter password length: ")), str(input("Enter delimiters: "))
            print(self.password(w, dl))

if __name__ == "__main__":
    phantom = GeneratePassword()
    phantom.main()
