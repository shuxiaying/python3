=pod
ProjectName: python3
FileName: he2
Author: TangJianjun
Date: 2020/8/24
Description:
=cut
#标量
$a=2;
print "\$a=$a\n";
#Here文档又称作heredoc、hereis、here-字串或here-脚本，
#是一种在命令行shell（如sh、csh、ksh、bash、PowerShell和zsh）
#和程序语言（像Perl、PHP、Python和Ruby）里定义一个字串的方法。
$var=<<"EOF";
这是一个here文档实列
可输入字符串和变量
如：a=$a
EOF
print "\$var=$var\n";
#数组
@arr=(1,2,3);
print "\$arr=@arr\n";
print "\$arr[0]=$arr[0]\n";
#哈希，无序的key=>value(或key,value)对集合
%h=('a'=>"a1",'b'=>2,'c'=>(1,2,3),'d'=>@arr);
print "\$h{'a'}=$h{'a'}\n";
print "\$h{'c'}=$h{'c'}\n";
print "\$h{'d'}=$h{'d'}\n";
#变量上下文
@arr2=@arr;#复制数组
print"\@arr2=@arr2\n";
$size=@arr;#数组赋值给标量，返回数组元素个数
print"\@arr的元素个数：$size\n";

