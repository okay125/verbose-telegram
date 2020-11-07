def area(a,b,c,d,anglesum):
    halfcir=(a+b+c+d)/2
    if a<0 or b<0 or c<0 or d<0 or anglesum<0 :
        print("参数必须非负哦！")
    elif a+b+c<d or a+b+d<c or a+c+d<b or b+c+d<a:
        print("构不成四边形哦！")
    elif anglesum>=360 :
        print("对角和必须小于360度哦！")
    else :
        import math
        C=(math.cos(math.radians(anglesum/2)))**2
        area4=math.sqrt((halfcir-a)*(halfcir-b)*(halfcir-c)*(halfcir-d)-a*b*c*d*C)
        print("四边形的面积是：",area4)
    return
a,b,c,d,anglesum=eval(input('请输入四边形的四条边长和一组对角和,中间以逗号分隔:'))
area(a,b,c,d,anglesum)
