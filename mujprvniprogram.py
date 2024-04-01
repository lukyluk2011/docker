print ("cau")

input ("ted ty (musis bez diakritiky a velkych pismen jako ja): ")

print ("co si myslis ze delam?")

odpoved = input ("ted ty (musis bez diakritiky a velkych pismen jako ja): ")

if odpoved == ("pisu ti"):
        print ("uhadl jsi, jsi dobrej, tak zase priste")
else:
        print ("chyba, ale nevadi, skus to znova")
        print ("co si myslis ze delam?")
        odpoved = input ("ted ty (musis bez diakritiky a velkych pismen jako ja): ")
        if odpoved == ("pisu ti"):
                print ("uhadl jsi, jsi dobrej, tak zase priste")
        else:
                print ("chyba, ale nevadi, skus to znova")
                print ("co si myslis ze delam?")
                odpoved = input ("ted ty (musis bez diakritiky a velkych pismen jako ja): ")
                if odpoved == ("pisu ti"):
                        print ("uhadl jsi, jsi dobrej, tak zase priste")
                else:
                        print ("chyba")
                        print ("prohrál jsi")
