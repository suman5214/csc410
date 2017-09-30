function method unpair ( i : nat ): ( nat , nat )

// unpair ( 0 ) = ( 0 , 0 )
// unpair ( 1 ) = ( 0 , 1 )
// unpair ( 2 ) = ( 1 , 0 )
// unpair ( 3 ) = ( 0 , 2 )
// unpair ( 4 ) = ( 1 , 1 )
// unpair ( 5 ) = ( 2 , 0 )
// unpair ( 6 ) = ( 0 , 3 )
// unpair ( 7 ) = ( 1 , 2 )
// unpair ( 8 ) = ( 2 , 1 )
// unpair ( 9 ) = ( 3 , 0 )
// unpair ( 10 ) = ( 0 , 4 )
// unpair ( 11 ) = ( 1 , 3 )
// unpair ( 12 ) = ( 2 , 2 )
// unpair ( 13 ) = ( 3 , 1 )
// unpair ( 14 ) = ( 4 , 0 )

{
if i == 0
    then (0,0)
else
    if n == 1
        then (0, 1)
    else
        if n == 2
            then (1, 0)
        else
            //recursive pattern
}

function method pick ( i : nat ): nat
{
var (x , y ) := unpair ( i );
x + i * y
}

method catchTheSpy ( a : nat , b : nat )
// decreases  a + i * b - i
decreases i
{
var i := 0;
while a + i * b != pick ( i )
{ i := i + 1; }
}
