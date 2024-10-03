from pickle import dump
p1={'resno':1001,"name":'Georgina Vance',"age":52,"status":"confirmed","no_oftickets":15}
p2={'resno':1002,"name":'Azaan Robbins',"age":23,"status":"pending","no_oftickets":14}
p3={'resno':1003,"name":'Bill Bucket',"age":35,"status":"confirmed","no_oftickets":26}
p4={'resno':1004,"name":'Eric Turner',"age":43,"status":"pending","no_oftickets":24}
p5={'resno':1005,"name":'Alvin Orr',"age":52,"status":"paid","no_oftickets":15}
p6={'resno':1006,"name":'Kyle Valdez',"age":52,"status":"paid","no_oftickets":15}
fh=open('tickets.dat','wb')
dump(p1,fh)
dump(p2,fh)
dump(p3,fh)
dump(p4,fh)
dump(p5,fh)
dump(p6,fh)
fh.close()
