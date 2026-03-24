print(r'''
              __   
           .-'  '-.       [Gillian]
          /        )                                 
          |  C   o( 
           \       >      
            )  \  /      ..`'
         .-._ / `'      /////     
        / _    \       ( | /
        |/ )    \\     / _,
        / /      |\   / /
       / /       | \ / /
      (  )       /\ ' /
       \ \      (  `-'
        \ \      Y 
        /\ `-.   |
        |(   ^'  |
        \ \\\\  /
         `-    f|
           |   ||
           |   f/
           j   /
           |   )
           |  |
           /  |
           f  |
           \  |
            | |&
           (   `-._,
            -^-----'
''')
print("Selamat datang di misi Penculikan Gillian.")
print("Anda adalah seorang penculik bayaran yang ditugaskan untuk menculik Gillian.")

qstn_1 = input("Anda sedang berada di sebuah pertigaan.\nKetik kanan untuk belok kanan atau kiri untuk belok kiri\n")
if qstn_1 == "kiri" or qstn_1 == "Kiri":
    qstn_2 = input("Anda menemukan sebuah pulau.\nKetik perahu untuk mencari perahu atau berenang untuk berenang.\n")
    if qstn_2 == "perahu" or qstn_2 == "Perahu":
        qstn_3 = input("Anda sampai di pulau dengan selamat.\nAda rumah yang mempunyai 3 pintu. Merah, Kuning dan Biru. Pintu mana yang anda pilih?\n")
        if qstn_3 == "kuning" or qstn_3 == "Kuning":
            print("Gillian ada di dalam ruangan tersebut dan anda berhasil menculiknya!")
        elif qstn_3 == "merah" or qstn_3 == "Merah":
            print("Gagal. Anda masuk ke ruangan Jehoiada.")
        elif qstn_3 == "biru" or qstn_3 == "Biru":
            print("Gagal. Anda masuk ke ruangan Justin.")
        else:
            print("Gagal. Anda tidak masuk ke salah satu ruangan.")
    else:
        print("Gagal.\nAnda tenggelam karena kelelahan.")
else:
    print("Gagal.\nAnda ditabrak kereta.")
