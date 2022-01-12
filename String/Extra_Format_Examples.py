# extra studies
a = 3
b = 4
print("The sum of {} + {} is : {}".format(a,b,a+b))

print("The multiplication of {} x {} is : {}".format(a,b,a*b))


print("The power of {} to {} is : {}".format(a,b,a**b))

# STRING FORMAT EXERCISE
text = "{:.2f}, {:.3f}, {:.4f}".format(3.1475, 5.3854, 7.1345422) # yuvarlama yapiyor. float icin .tadan sonra kac karakter alinacak onu gosteriyor
print("Ex1: " + text)

text = "{:.2s}, {:.3s}, {:.4s}".format("3a.1415", "5.b3854", "7.1345422c") # toplamda kac karakter alinacak onu gosteriyor
print("Ex2: " + text)

text = "{:.2}, {:.3}, {:.4}".format("3a.1415", "5.b3854", "7.1345422c") # yukaridaki ile ayni "s"i yazmamiz gerekmiyor
print("Ex3: " + text)

# verilen kelime belirlenmis satirin en sagkismini dolduracak
# ex: 10 karakterlik bir bosluga test kelimesini ekle
text = "{:>10}".format("test")
print(text)

text = "{:<10}".format("deneme")
print(text)

text = "formatlama methodu {:<20} son kismi".format("test")
print(text)

# yazimizi ortalamak istersek
text = "formatlama methodu {:^20} son kismi".format("test")
print(text)

print("{:10.5}".format("hippopotamus"))

print("{:>15.5}".format("hippopotamus"))

print("{:+}".format(55))