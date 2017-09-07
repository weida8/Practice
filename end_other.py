def end_other():
 a=str(input("a:"))
 b=str(input("b:"))
 anew=str.lower(a)
 bnew=str.lower(b)
 print(anew)
 print(bnew)
 short=min(anew, bnew)
 longletter=max(anew, bnew)
 print(short)
 print(longletter)
 if(longletter.endswith(short)):
  print(True)

end_other()
