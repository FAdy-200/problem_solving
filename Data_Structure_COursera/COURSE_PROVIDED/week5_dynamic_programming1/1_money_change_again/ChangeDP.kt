import java.util.*

fun getChange(m: Int): Int {
    //write your code here
    return m / 4
}

fun main(args: Array<String>) {
    val scanner = Scanner(System.`in`)
    val m = scanner.nextInt()
    println(getChange(m))
}