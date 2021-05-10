---
title: C++学习笔记(五)
mathjax: true
categories:
  - C++ 学习
  - 基础知识
tags:
  - C++
  - 基础
abbrlink: 2c61a387
date: 2021-05-10 11:03:12
---

<meta name = "referrer" content = "no-referrer" />

![](https://wx4.sinaimg.cn/mw690/0083TyOJly1gqd3zdkobvj31hc0u0u10.jpg)

<!-- less -->

# C++ 学习笔记（五）

## C++类型转换

尽量少使用类型转换，除非用来解决特殊问题

### 静态转换`static_cast`

```cpp
目标类型 目标对象 = static_cast<目标类型>(原对象);
```

- 用于类层次结构中的基类和派生类之间指针或引用的转换，没有父子关系的不能转换
  - 进行上行转换（派生类的指针或引用转换成基类）是安全的
  - 进行下行转换（基类指针或引用转换成派生类）时，由于没有动态类型检查，所以时不安全的

- 用于基本数据类型之间的转换，如将`int`转换成`char`，把`char`转换成`int`，这种转换的安全性也要开发人员来保证

### 动态转换`dynamic_cast`

`dynamic_cast`非常严格，失去精度或者不安全都不可以转换

```cpp
目标类型 目标对象 = dynamic_cast<目标类型>(原对象);
```

- 基础类型之间不能转换

- `dynamic_cast`如果发生了多态，那么可以让基类转为派生类，向下转换

### 常量转换`const_cast`

用来修改`const`属性

- 常量指针被转化成非常量指针，并且仍然指向原来的对象
- 常量引用被转换成非常量引用，并且仍然指向原来的对象

**注意**:不能直接对非指针和非引用的变量使用`const_cast`操作符去直接移除它的`const`

```cpp
const int * p = NULL;
int *newp = const_cast<int *> (p);
int * p1 = NULL;
const int *newp1 = const_cast<const int *> (p1);
```

### 重新解释转换`reinterpert_cast`

最不安全，不推荐使用

 ## 异常

```cpp
try{
    // 试图执行的内容
    // 在可能出现异常的地方抛出异常throw
}
catch() {
 	// try下面catch捕获异常   
    // catch(捕获类型) ... 代表所有其他类型
    // 如果不想处理异常，继续向上抛出throw
}
```



### 跳级

![image-20210510100605400](https://wx4.sinaimg.cn/mw690/0083TyOJly1gqd3vb0ulnj30im0ex3zy.jpg)

### 异常基本处理

```cpp
int myd(int a, int b){
	if(b == 0) {
        // return -1; 早期处理方式，返回-1
        throw -1; // 抛出int类型异常，异常必须处理，如果不处理就挂掉
    }
    return a/b;
}
void test() {
    int a = 10, b = -10;
    int ret =  myd(a, b); // 早期如果返回-1， 无法区分到底是结果还是异常
    try{
        myd(a, b);
    }
    catch(int) {// 捕获int类型异常
        // 如果不想在这处理，就抛出，返回上一层处理,类型不变
        throw;
    	//. 异常处理
    }
    catch(...) { //其他类型异常捕获
        
    }
}
void test2() {
    try{
        test();
    }catch(int) { // 如果异常都没有处理，那么成员terminate函数是程序中断
        // ...
    }
}
```

### 自定义异常类

```cpp
class MyException{
    public :
      void printError();
}
// try{ 抛出异常
//	throw MyException();
// }
// 捕获异常
catch(MyException e) {
    e.printError();
}
```

### 栈解旋

- 从try开始到throw抛出异常之前，所有栈上的对象，都会被释放，这个过程称为栈解旋
- 栈上对象构造和析构顺序相反

### 异常的接口声明

```cpp
void func() throw(int) { //thrwo(int) 只能抛出int类型异常
    throw 3.14;
    // 抛出double类型直接挂掉
}
void func() throw() { //thrwo() 不跑出任何类型异常
    throw 3.14;
}
```

### 异常变量声明周期

异常变量的构造是在`throw`抛出异常时构造，析构实在`catch`处理完以后析构

```cpp
class MyException{
    public :
      void printError();
}
void dowork() {
    throw MyException();
}
void test() {
    try {
        dowork();
    }catch(MyException e) { // catch时通过拷贝构造又会有一份数据，所以建议使用& 
        // catch(MyException &e)
        
    }
}
// 返回指针，使用new，在堆区开辟内存，然后手动delete
void dowork() {
    throw new MyException();
}
void test() {
    try {
        dowork();
    }catch(MyException * e) { // catch时通过拷贝构造又会有一份数据，所以建议使用& 
        // catch(MyException &e)
        delete e;
    }
}
```

### 异常的多态

利用多态来实现`printError`同一个接口的使用

### 系统的异常库

```cpp
#include <stdexcept>
```

## 文件读写

### 头文件

```cpp
#include <fstream>
```

### 写文件

```cpp
void test() {    ofstream ofs(path， ios::out|ios::trunc);    if(!ofs.is_open) {        //... 打开失败    }    ofs << "content" << endl;}
```

### 读文件

```cpp
void test() {    ifstream ifs(path, ios::in);    if(!ifs.is_open) {        //... 打开失败    }    // 第一种方式    char buf[1024];    while(ifs >> buf) { // 按行读取        cout << buf << endl;    }    // 第二种方式    while(!ifs.enf()) { // enf读到文件尾        ifs.getline(buf, sizeof(buf));        cout << buf  << endl;    }    // 第三种方式 不推荐 按单个字符读取    char c;    while((c = ifs.get()) != EOF) {        cout << c << endl;    }    }
```

