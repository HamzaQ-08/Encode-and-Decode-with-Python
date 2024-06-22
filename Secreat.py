#Code
try:
  giv=input("1.For Coding Type 1\n\n2.For Decoding type 2\n\n3.For Quitting Type quit or 0: ")

  if giv=="quit" or giv=="0":
    print("\nThanks for using")

  elif giv=="1":
    a=(input("\nInter a code: "))
    words=a.split()
    if (len(a)>3):
      fir=a[0]
      sec=a[-1]
      thr=a[-2]
      fur=a[2]
      add= sec + fir + fur + a[::-1] + a[0] + sec+ thr +fir
      print(add)
  
    elif (len(a)<=3):
      print(a[::-1]+a[1]+a[0])
    
#Decode
  elif giv=="2":
    b=(input("\nInter for decode: "))
    words=b.split()

    if (len(b)>5):
      fer=b[3:-4]
      sic=b[::-1]
      thi=b[:-4]
      fi=fer[::-1]
      print("\n",fi)

  elif (len(b)<=5):
    rev=b[:-2]
    print(rev[::-1])
    
except:
  print("Invalid Input")
    



  
