char1="t"
char2="s"
def lang(x):
        for char in x:
                char1 += 1
                char2 += 1
        if char1 > char2:
            print("English")
        elif char2 > char1:
            print("FRENCH")
# lang("Silver, why are you so sad?")
lang=("Lorsque j'avais six ans j'ai vu, une fois,")

