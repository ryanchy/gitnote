js直接量

//空字符串直接量
1  //数值直接量
true  //布尔值直接量
/a/g  //正则表达式直接量
null  //特殊值直接量
{}  //空对象直接量
[]  //空数组直接量
function(){}  //空函数直接量，也就是函数表达式


转义序列
转义序列就是字符的一种表示方式（映射）。由于各种原因，很多字符无法直接在代码中输入或输出，只能通过转义序列间接表示。
Unicode 转义序列方法：\u + 4位十六进制数字。
Latin-1 转义序列方法：\x + 2位十六进制数字。
示例
对于字符“©” , Unicode 转义为 \u00A9，ASCII 转义为 \xA9。
document.write("\xa9");  //显示字符©
document.write("\u00a9");  //显示字符©

标识符
标识符（Identifier）就是名称的专业术语。JavaScript 标识符包括变量名、函数名、参数名和属性名。

合法的标识符应该注意以下强制规则：
第一个字符必须是字母、下划线（_）或美元符号（$）。
除了第一个字符外，其他位置可以使用 Unicode 字符。一般建议仅使用 ASCII 编码的字母，不建议使用双字节的字符。
不能与 JavaScript 关键字、保留字重名。
可以使用 Unicode 转义序列。例如，字符 a 可以使用“\u0061”表示。
示例
在下面示例中，定义变量 a，使用 Unicode 转义序列表示变量名。
var \u0061 = "字符 a 的 Unicode 转义序列是 \\0061";
document.write(\u0061);

使用转义序列不是很方便，一般常用转义序列表示特殊字符或名称，如 JavaScript 关键字、程序脚本等。
关键字
关键字就是 ECMA-262 规定的 JavaScript 语言内部使用的一组名称（或称为命令）。这些名称具有特定的用途，用户不能自定义同名的标识符。具体说明如表所示。

ECMAScript 关键字
break	delete 	if	this 	while
case	do	in	throw	with
catch 	else 	instanceof 	try	 
continue 	finally 	new 	typeof	 
debugger（ECMAScript 5 新增）	for 	return 	var	 
default 	function 	switch 	void	 
保留字
保留字就是 ECMA-262 规定的 JavaScript 语言内部预备使用的一组名称（或称为命令）。这些名称目前还没有具体的用途，是为 JavaScript 升级版本预留备用的，建议用户不要使用。具体说明如表所示。

ECMAScript 保留字
abstract 	double 	goto 	native 	static
boolean 	enum 	implements 	package 	super
byte 	export 	import 	private 	synchronized
char 	extends 	int 	protected 	throws
class 	final 	interface 	public 	transient
const 	float 	long 	short 	volatile
ECMAScript 3 将 Java 所有关键字都列为保留字，而 ECMAScript 5 规定较为灵活。

例如，在非严格模式下，仅规定 class、const、enums、export、extends、import、super 为保留字，其他 ECMAScript 3 保留字可以自由使用；在严格模式下，ECMAScript 5 变得更加谨慎，严格限制 implements、interface、let、package、private、protected、public、static、yield、eval（非保留字）、arguments（非保留字）的使用。

JavaScript 预定义了很多全局变量和函数，用户也应该避免使用它们。具体说明如表所示。

JavaScript 预定义全局变量和函数
arguments 	encodeURL 	Infinity 	Number 	RegExp
Array 	encodeURLComponent 	isFinite 	Object 	String
Boolean 	Error 	isNaN 	parseFloat 	SyntaxError
Date 	eval 	JSON 	parseInt 	TypeError
decodeURL 	EvalError 	Math 	RangeError 	undefined
decodeURLComponent 	Function 	NaN 	ReferenceError 	URLError
不同的 JavaScript 运行环境都会预定义一些全局变量和函数，上表列出的仅针对 Web 浏览器运行环境。
