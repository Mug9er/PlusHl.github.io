---
title: C++学习笔记(四)
mathjax: true
date: 2021-05-08 18:29:45
categories:
  - C++ 学习
  - 基础知识
tags:
 - C++
  - 基础
---

<meta name = "referrer" content = "no-referrer" />

![](https://wx4.sinaimg.cn/mw690/0083TyOJly1gqb73euj9aj30u015ohdz.jpg)

<!-- less -->

# C++学习笔记（四）

## 继承

```cpp
class 子类 : 继承方式 父类
```

### 继承权限

| 继承方式  |           特点            | 父类私有属性能不能访问 |
| :-------: | :-----------------------: | :--------------------: |
| `public`  |    父类的属性权限不变     |          不能          |
| `protect` | 父类的属性全变为`protect` |          不能          |
| `private` | 父类的属性全变为`private` |          不能          |

子类中会继承父类的私有成员，但是被编译器隐藏了起来

### 继承中的构造与析构

```cpp
构造： 先执行父类的构造函数，在调用子类的构造函数

析构：先执行子类的析构，在执行父类的析构
```

子类并不能继承父类的构造和析构函数，只有父类自己知道自己构造和析构的属性

如果父类没有默认构造，那么子类在构造时可以通过初始化列表的方式显示调用父类的有参构造

```###  
class Base{
	Base(int a) ;
}
class Son : public Base{
	Son(int a): Base(a) {
} 
}
```

### 继承中的同名处理

子类与父类属性或函数同名时，根据就近原则，属性为子类的值，如果想使用父类的值，那么就在调用时加上作用域

```cpp
class Base{
    public:
int m_a;
}
class Son : punlic Base{
    public;
    Son(int a) {
        this->m_a = 200;
    }
    int m_a;
}
void test() {
    Son s;
    cout << s.m_a << endl; // 子类的m_a
    cout << s.Base::m_a << endl;// 父类的m_a
}
```

如果子类与父类的成员函数名称相同，子类会把父类的所有同名版本全隐藏，像调用父类的方法，必须加作用域

### 继承中的静态成员处理

静态成员属性，子类可以继承下来，使用时直接在静态成员属性前加作用域即可

静态成员函数，子类也可以继承下来，使用时

```cpp
Son::func() // 子类的func
Son::Base::func() // 父类的func
```

### 非自动继承的函数

不是所有的函数都能继承到子类，构造和析构函数不能继承，`operator=`也不能继承，因为它完成类似构造函数的行为

### 多继承

一个类可以继承多个类

```cpp
class A: public B, public C
```

#### 二义性

多继承中如果多继承的多个类有相同的成员属性，那么子类在调用父类相同的属性时会引发二义性

```cpp
class A: public B, public C
A a;
cout << a.m_a << endl; // 如果B和C中都有m_a会引发二义性
cout << a.B::m_a << a.C::m_a << endl;// 使用时在前面加上作用域
```

### 菱形继承

子类继承的父类继承自同一个基类，会导致二义性的产生

```cpp
class A;
class B: public A;
class C: public A;
class D: public B, public C;
```

### 菱形继承解决方案

#### 虚继承

```cpp
class A;
class B: virtual public A; //虚基类B
class C: virtual public A; // 虚基类C
class D: public B, public C;
```

虚继承后，子类中会有一个虚指针，指向一张虚基类表，通过表找到偏移量可以找到共有数据

## 多态

多态分为编译时多态（静态多态）和运行时多态（动态多态），运算符重载和函数重载是编译时多态，派生类和虚函数是运行时多态

- 静态联编： 地址早绑定，编译阶段绑定好地址
- 动态联编： 地址晚绑定，运行时绑定号地址
- 多态： 父类的引用或指针 指向子类对象

```cpp
class Animal {
public:
	virtual void speak() {
		cout << "animal speak" << endl;
	}
};

class Cat : public Animal {
public:
	void speak() {
		cout << "cat speak" << endl;
	}
};

// 调用dospeak，没有使用virtual时 speak函数的地址早就绑定好了，静态联编， 编译阶段确定好了地址
// 如果想使用cat的speak，那么就不能提前绑定函数的地址，所以需要运行时确定函数地址
// 动态联编，写法 dospeak 改为虚函数，在父类上声明虚函数，发生了多态
// 父类的引用或指针 指向子类对象
void doSpeak(Animal& animal) { // 使用虚函数时 Animal & animal = cat	
	animal.speak();
}

void test() {
	Cat cat;
	//如果发生了继承，编译器允许进行类型转换
	doSpeak(cat);
}
```

![image-20210508173802580](https://wx2.sinaimg.cn/mw690/0083TyOJly1gqb74bih29j30tx0hu43x.jpg)

当`Animal`有了虚函数后，内部结构发生了改变， 内部多了一个虚指针，指向`Animal`的虚函数表 ,`Cat`内部也有一个虚指针，继承自`Animal`的虚指针，指向自己内部的虚函数表，父类和子类的虚函数表相同但是地址不同。如果`Cat`没有重写`Animal`的`speak`函数，那么虚函数表中的函数就是`Animal`的`speak`，如果重写了，那么就是`Cat`自身的`speak`

```cpp
Animal * animal = new Cat;
animal->spead()；
// 调用的是cat的speak，因为父类指针指向子类对象，指向时，子类已经发生多态，调用的也是多态后的函数
```

### 纯虚函数

```cpp
virtual int abc() = 0; // 告诉编译器在vtable中保留一个位置
```

如果父类有纯虚函数，那么子类必须实现纯虚函数

如果父类有了纯虚函数，那么父类就无法实例化对象，变成抽象类

 ### 虚析构和纯虚析构

普通析构函数是不会调用子类的析构的，所以可能导致释放不干净，虚析构可以解决这个问题

纯虚析构需要声明并且实现，在类内声明，在类外实现，只声明不实现会报错，如果类出现了纯析构函数，那么这个类也算抽象类

### 类型转换

- 基类转派生类，向下转换，不安全

  ```cpp
  Animal * animal = new Animal;
  Cat *cat = (Cat*)animal;
  ```

- 派生类转基类，向上转换，安全

  ```cpp
  Cat * cat = new Cat;
  Animal *animal = (Animal*)cat;
  ```

- 如果发生了多态，总是安全的