s_triangle = input().split()

a = int(sorted(s_triangle)[0])
b = int(sorted(s_triangle)[1])
c = int(sorted(s_triangle)[2]) #max


if a+b <= c:
    print('삼각형이 아닙니다.')
else:  #삼각형
    if len(set(s_triangle))==1:
        print('정삼각형')
    elif len(set(s_triangle))==2:
        print('이등변삼각형')
    elif a**2+b**2==c**2:
        print('직각삼각형')
    else:
        print('삼각형')
