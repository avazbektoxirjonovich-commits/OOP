class student:
    def __init__(self,ism,familya,yonaliw,bosqich):
        self.ism=ism
        self.familya=familya
        self.yonaliw=yonaliw
        self.bosqich=bosqich

    def chek_exam(self,ball):
        if ball >= 70:
          self.bosqich+=1
          print("Tabriklaymiz otdingiz")
        else:
            print("Imtihondan otolmadingiz , bosqichni qayta oqisiz")
    def info(self):
        print(f"Ism: {self.ism}")
        print(f"Familya: {self.familya}")
        print(f"Yonalish: {self.yonaliw}")
        print(f"Bosqich: {self.bosqich}")

student1=student("ali ","valiyev",1,2)
student1.chek_exam(75)
student1.info()
