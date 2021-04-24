class Leaf :
    def __init__( self, value ) :
        self.value = value

class Tree :
    def __init__( self ) :
        self.ur = None
        self.ul = None
        self.dl = None
        self.dr = None

def populate( data, xm, xM, ym, yM ) :
    
    flag = True
    a, b = False, False

    for i in range( xm, xM + 1 ) :
        for j in range( ym, yM + 1 ) :
            if data[i][j] == 0 :
                a = True
            else :
                b = True
            if a and b :
                flag = False
                break
        if not flag : break

    if flag :
        return Leaf( data[xm][ym] )

    x = Tree()
    
    if xM - xm == 1 :
        x.ur = Leaf( data[ym][xM] )
        x.ul = Leaf( data[ym][xm] )
        x.dl = Leaf( data[yM][xm] )
        x.dr = Leaf( data[yM][xM] )
        return x
    else :
        x.ur = populate( data, (((xM + 1)-xm)//2)+xm, xM, 0, ((yM+1)//2)-1 )
        x.ul = populate( data, 0, ((xM+1)//2)-1, 0, ((yM+1)//2)-1 )
        x.dl = populate( data, 0, ((xM+1)//2)-1, (((yM + 1)-ym)//2)+ym, yM )
        x.dr = populate( data, (((xM + 1)-xm)//2)+xm, xM, (((yM + 1)-ym)//2)+ym, yM )
    return x



def found( data, x, y, xmin, xmax, ymin, ymax ) :
    if type( data ) == Leaf :
        #print( "here", x, y, "-", xmin, xmax, ymin, ymax )
        return data.value
    if x > (xmin + xmax)/2 :
        if y < (ymin + ymax)/2 :
            return found( data.ur, x, y, xmin + (xmax+1-xmin)//2, xmax, ymin, ymax - (ymax+1-ymin)//2 )
        else :
            return found( data.dr, x, y, xmin + (xmax+1-xmin)//2, xmax, ymin + (ymax+1-ymin)//2, ymax )
    else :
        if y < (ymin + ymax)/2 :
            return found( data.ul, x, y, xmin, xmax - (xmax+1-xmin)//2, ymin, ymax - (ymax+1-ymin)//2 )
        else :
            return found( data.dl, x, y, xmin, xmax - (xmax+1-xmin)//2, ymin + (ymax+1-ymin)//2, ymax )


def printT( tree, xmax, ymax ) :
    for y in range( 0, ymax+1 ) :
        for x in range( 0, xmax+1 ) :
            #print( "----", x, y, end=" " )
            print( found( tree, x, y, 0, xmax, 0, ymax ), end=" " )
        print( "" )




def count( tree ) :
    if type( tree ) == Leaf :
        return 1
    return count( tree.ur ) + count( tree.ul ) + count( tree.dl ) + count( tree.dr )

def higher_leaf( tree ) :
    if type( tree ) == Leaf :
        return 0
    return 1 + min( higher_leaf( tree.ur ), higher_leaf( tree.ul ), higher_leaf( tree.dl ), higher_leaf( tree.dr ) )

def operate( tree ) :
    if type( tree ) == Leaf :
        return tree.value
    else :
        ur = operate( tree.ur )
        ul = operate( tree.ul )
        dl = operate( tree.dl )
        dr = operate( tree.dr )
        if ur + ul + dl + dr == 2 :
            return 0
        else :
            return 1

def collapse( tree, depth ) :
    if type( tree ) == Leaf :
        return tree
    if not depth :
        return Leaf( operate( tree ) )
    else :
        tree.ur = collapse( tree.ur, depth - 1 )
        tree.ul = collapse( tree.ul, depth - 1 )
        tree.dl = collapse( tree.dl, depth - 1 )
        tree.dr = collapse( tree.dr, depth - 1 )
    return tree

data1 = [[1,1], [1,0]]
data2 = [[1,1], [1,1]]
data3 = [[0,0], [0,0]]
data4 = [[1,0], [0,0]]
data5 = [[1,1,0,1],[1,1,0,1],[1,0,0,1],[1,0,1,1]]
x = populate( data5, 0, 3, 0, 3 )

for i in range( len( data5 ) ) :
    for j in range( len( data5 ) ) :
        print( data5[i][j], end=" ")
    print("")

print( "" )
print( x.dr.ul.value, x.dr.ur.value )
print( x.dr.dl.value, x.dr.dr.value )

print( "" )
printT( x, 3, 3 )

#print( "" )
#printT( x, 3, 3 )

#print( count( x ) )
#print( higher_leaf( x ) )

y = collapse( x, 1 )
#printT( y, 1, 1 )