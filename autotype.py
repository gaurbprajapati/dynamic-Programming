import keyboard as key
key.wait("esc")
a = """


package q11117;
public class Box {
// Declare variables
float l,b,h;
public Box(float l, float b, float h) {
// Write the code
this.l=l;
this.b=b;
this.h=h;
}
public float volume() {
// Write the code
return l*b*h;
}
public int compare(Box b) {
// Write the code
if(this.volume()>b.volume()) return 1;
else return -1;
}
public static void main(String args[]) {
int flag;
Box box1 = new Box(Float.parseFloat(args[0]), Float.parseFloat(args[1]), Float.parseFloat(args[2]));
Box box2 = new Box(Float.parseFloat(args[3]), Float.parseFloat(args[4]), Float.parseFloat(args[5]));
flag = box1.compare(box2);
if (flag == 1)
System.out.println("box1 is larger than box2");
else if (flag == 0)
System.out.println("box1 is same size as box2");
else
System.out.println("box1 is smaller than box2");
}
}



"""
key.write(a, exact=True, delay=0.05)
