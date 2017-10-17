# PRG -- na začátek B

## Obrázky

Vytvořte program který vytiskne na tyto obrázky o zadaném počtu řádků:

    ****
    ***
    **
    *

        *
       ***
      *****
     *******
    ********* 

    *
    **
    ***
    ****
    ***
    **
    *

## Řady čísel

V následujících případech se vždy pracuje s posloupností čísel. Pokud si chcete
usnadnit práci při jejich zadávání (psát to pořád dokola může být nuda) můžete
si čísla nechat generovat náhodně:

```python
import random
# generuje 20 náhodných čísel od 1 do 50 
seznam = [random.randint(1,50) for i in range(20)] 
```

1. Je dána posloupnost celých kladných čísel. Určete kolik z nich je sudých.

2. Je dána posloupnost celých kladných čísel. Vypište ta, která jsou větší než 11 a menší než 19

3. Je dána posloupnost celých kladných čísel. Vypište ta, která jsou dělitelné zároveň 3 a 4.

4. Je dána posloupnost celých čísel. Vypište celkový součet kladných a celkový součet záporných čísel.

```
zadej čísla > 1 -2 3 -4 8 -3
>>>>>>>>>>>>>  kladná: 12
>>>>>>>>>>>>> záporná: -9
```

5. Je dána posloupnost celých čísel. Vypište na obrazovku součet jejich
druhých mocnin.

```
zadej čísla > 1 -2 4
>>>>>>>>>>>>> 21
```

6. Je dána posloupnost kladných čísel. Vypočítejte jich aritmetický průměr.


## Fibonacciho posloupnost

Vytvořte program, který vytiskne prvních *n* prvků
[Fibonacciho posloupnosti](https://cs.wikipedia.org/wiki/Fibonacciho_posloupnost).
Ta je tvořena je tvořena jednoduchými pravidly:

 * první prvek je vždy 0
 * druhý prvek je vždy 1
 * každý následující prvek je součtem předchozích dvou prvků

![](img/fib.svg)

## Pascalův trojúhelník

Vytvořte program, který vytiskne prvních *n* řádků
[Pascalova trojúhelníku](https://cs.wikipedia.org/wiki/Pascal%C5%AFv_troj%C3%BAheln%C3%ADk).
Problém lze řešit složitější matematikou pomocí kombinačních čísel, ale 
plně si vystačíte i s normálním sčítáním

Výstup může vypadat například takto:

                1
              1   1
            1   2   1
          1   3   3   1
        1   4   6   4   1
      1   5  10  10   5   1
    1   6  15  20  15   6   1

