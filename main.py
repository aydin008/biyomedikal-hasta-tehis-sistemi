hastaliklar = {
    "BRCA1": "Meme kanseri riski",
    "CFTR": "Kistik Fibrozis"
    }

hasta_dna = "ATGCGXATC"
uzunluk = len(hasta_dna)
print("DNA uzunluğu: " , uzunluk)

if "X" in hasta_dna:
        print("HASTANIN DNA'SINDA MUTASYON MEVCUT!")
else: 
        print("Hastanın DNA'sında sıkıntı yok.")

rna = hasta_dna.replace("T" , "U")
print("Hastanın RNA'sı: " , rna)

tespit_edilen_gen = "BRCA1"
if tespit_edilen_gen in hastaliklar:
    print("Gen hastada tespit edildi: " , hastaliklar[tespit_edilen_gen])


nabizlar = [55, 75, 115, 80] 
for nabiz in nabizlar:
    if nabiz > 100:
        print("Yüksek nabız!")
    elif nabiz < 60:
        print("Düşük nabız!")
    else:
        print("Normal nabız.")

ort_nabiz = sum(nabizlar) / len(nabizlar)
print("Ortalama nabız: " , ort_nabiz )
