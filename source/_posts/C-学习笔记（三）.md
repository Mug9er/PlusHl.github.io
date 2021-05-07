---
title: C++学习笔记（三）
mathjax: true
date: 2021-05-07 10:54:05
categories:	
    - C++ 学习
    - 基础知识
tags:
	- C++
	- 基础
---

<meta name = "referrer" content = "no-referrer" />

![](https://wx3.sinaimg.cn/mw690/0083TyOJly1gq9ob4y7xvj31o00u07wh.jpg)

<!-- less -->

# C++ 学习笔记(三)

## 静态成员

### 静态成员变量

​		在一个类中，若将一个成员变量声明为`static`，这种成员成为静态变量，与一般的数据成员不同，无论建立了多少个对象，都只有一个静态数据的拷贝，静态成员变量，属于某个类，所有对象共享。

​		静态变量，是在编译阶段就分配空间，对象还没有创建时，就已经分配空间。

- 静态成员变量必须在类中声明，在类外定义
- 静态数据成员 不属于某个对象，在为对象分配空间中不包括静态对象成员所占空间
- 静态数据成员可以通过类名或者对象名来引用
- 静态成员变量在类内声明，在类外初始化
- 静态成员变量也有权限

### 静态成员函数

- 静态成员函数不可以访问普通的成员变量，可以访问静态成员变量
- 静态成员函数也是有权限的
- 普通成员函数可以访问普通成员变量，也可以访问静态成员变量    

## 面向对象模型初探

### 成员变量和函数的存储

数据 和 处理数据的操作是分开存储的

- `C++`中的非静态数据成员直接内含在类对象中，就像`C struct`一样
- 成员函数虽然内含在`class`声明之内，却不出现在对象中
- 每一个非内联成员函数只会诞生一份函数实例

空类的大小为1,每一个实例的对象，都有独一无二的地址，`char`维护这个地址

```cpp
class Person{
public:
    int m_A; // 非静态成员变量，属于对象身上
    void func() {}; //非静态成员函数，不属于对象身上
   	static int m_B; // 静态成员变量，不属于对象身上
    static void func2() {}; //静态成员函数，不属于对象身上
}
// 结论： 非静态成员变量，才属于对象身上
```

### `this`指针

`this`指针称为“永远指向本对象的指针”，`this`指针并不是对象的一部分,`*this`是对象本体

`this`指针是一种隐含指针，它隐含于每个类的非静态成员函数中，静态成员函数不能访问`this`指针

`this`指针指向被调用的成员函数所属的对象

```cpp
Person p1;
p1.func(Person*this);// 编译器会偷偷加上一个p1的this指针
```

#### 空指针访问成员函数

空指针可以访问成员函数，但是如果成员函数中用到了`this`指针，那么就会执行失败

#### `const` 修饰成员函数

`this`永远指向本体，类似`Person * const this`,`this`的指向不能修改，但指针指向的值可以修改

```cpp
void showInfo() const { // const加后面代表常函数，意味着不允许修改指针指向的值
    this->m_B = 100; // 如果在常函数中修改，那么就在成员变量前面加mutable
}
mutable int m_B;
```

#### 常对象

常对象不允许修改属性

```cpp
const Person p2;
```

常对象不可以调用普通的成员函数，可以调用常函数

## 友元

友元函数可以访问类的私有成员属性

### 全局函数做友元

全局函数可以作为类的友元函数，在类中声明全局函数，并加上`friend`关键字

```cpp
class A{
    public:
    friend void test();
};
void test() {
    // ...
}
```

### 类做友元

```cpp
class A{
	friend class B;
    // B作为A的友元类，可以访问A的私有成员属性
}
```

### 成员函数做友元

```cpp
class A{
    firend void B::test();
    // B的成员函数作为A的友元，可以访问A的私有成员属性
}
```

## 运算符重载

如果想让自定义数据类型进行运算符运算，那么就需要重载运算符。

在成员函数或者在全局函数中，重写一个运算符重载，运算符重载也可以进行重载

**对于内置数据类型的表达式运算符是不可以改变的（例如int类型的+号）**

### `+`号重载

```cpp
class A {
    // 类内重载
    A operator + (A & b) {
        A tmp;
        // ...
        return tmp;
    }
}
// 全局重载
A operator + (A &a, A &b) {
    A tmp;
    // ...
    return tmp;
}
```

### `<`左移运算符

不要随意使用符号重载，`cout << `可以对自定义数据类型进行输出

```cpp
ostream& operator << (ostream &cout, A &a) { // 第一个参数cout，第一个参数A    
    cout << "A: " << a << endl;
}//全局重载可以在类中添加friend，访问类的私有成员属性
```

### 前置后置递增运算符重载

```cpp
class MyInt{  // 前置++重载
    MyInt& operator++(){    this->num ++;    return *this;}// 后置++重载，使用int来区分
    MyInt operator++(int) {    MyInt tmp = *this;    this->num ++;    return tmp;}private:   int  num;}
```

### 指针运算符重载

智能指针，用来托管自定义类型对象，让对象进行自动的释放

智能指针就是一个包含对象类型的类，重载`->`可以使得智能指针调用类内指针的成员函数以及成员变量

```cpp
A * operator -> () { // 加上*代表返回指针    
    return this->a;
}
A & operator * () {    
    return *this->a;
}
```

### 赋值运算符重载

一个类默认创建，默认构造、析构、拷贝构造 、`operator=`赋值元算符

```cpp
class Person {    // 重载=    
    Person& operator = (const Person& p) {       
        //先判断堆区是否有内容       
        if (this->pName != NULL) {            
            delete[] this->pName;            
            this->pName = NULL;        
        }        
        this->pName = new char[strlen(p.pName)+1];        
        strcpy(this->pName, p.pName);        
        return *this;   
    }    
    private:    char* pName;
}
```

### []重载

```cpp
class MyArray{ 
    public:    
              // []重载	
              int& operator[] (int   idx) {		
                  return *this->pAddress[idx];   
              }   private:    
    int *pAddress;    
    int m_Size;   
    int m_Capacity;
};
```

### 关系运算符重载

```cpp
class Person{    
    bool operator == (Person &p) {		
        if(this->name == p.name && this->age == p.age) {     
            return true;     
        }       
        return false;   
    }   
    bool operator != (Person &p) {	
        if(this->name == p.name && this->age == p.age) {   
            return false; 
        }      
        return true;   
    }public:      
    string name; 
    int age;   
}
```

### 函数调用运算符

()重载

```cpp
class MyPrint{
    public: 
    void operator() (string s) {   
        cout << s << endl; 
    }
}
MyPrint mp;//仿函数
MyPrint()("你好") 
mp("你好");// 匿名对象
```

### 总结

- =， []，-> 操作符只能通过成员函数进行重载
- <<，>>只能通过全局函数配合友元函数重载
- 不要重载&&，||操作符，因为无法实现短路规则