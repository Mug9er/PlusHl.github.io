---
title: C++学习笔记(二)
mathjax: true
categories:
  - C++ 学习
  - 基础知识
tags:
  - C++
  - 基础
abbrlink: 5287e3ee
date: 2021-05-04 14:21:25
img: https://cdn.jsdelivr.net/gh/Mug-9/imge-stroage@master/cover/wallhaven-1kqj9g.32bye91jnew0.jpg
---

# C++学习笔记（二）

## 类

类是对对象的抽象

对象是对类的实例

```cpp
class 类名{
public: 公共权限
    设置 成员属性
    设置 成员函数
}
```

### 设计一个圆类，求圆的周长

```cpp
/*
设计一个类，求圆的周长
*/
const double pi = 3.1415926535;

class Circle{ //class 代表声明一个类，后面紧跟的是类的名称
  public: //公共权限
  // 半径 成员属性
    int  m_R;
    // 求圆周长的函数
    double calZC() { // 类里面的函数，叫作成员函数
      return 2 * pi * m_R;
    }
    // 设置半径的成员方法 成员函数通常可以修改成员属性
    void setR(int r) {
      m_R = r;
    }
};
```

### 设计学生类

```cpp
class Student {
public:
  string m_Name; // 姓名
  int m_Id;  // 学号

  void  setName(string name) {
    m_Name = name;
  }

  void setId(int id) {
    m_Id = id;
  }

  void showInfo() {
    cout << "姓名:" << m_Name << " 学号:" << m_Id;
  }
};
```

## 内联函数

​		宏函数只是简单的在编译期进行替换，所以宏函数无法对传参进行检查，也会出现歧义。内联函数是一个真正的函数，会检查函数参数列表，并返回值。内联函数在编译期也会进行替换，所以内联函数会占用空间，但是内联函数相对于普通函数的优势是省去了函数调用时的压栈，跳转和返回的开销。我们可以理解为内联函数以空间换时间。类中的成员函数默认是内联函数。

​		内联仅仅是给编译器的一个建议，编译器不一定会接受这种建议，如果你没有江汉数声明为内联函数，那么编译器也可能将此函数做内联编译，一个好的编译器将会内联小的、简单的函数。

## 函数默认参数

```cpp
void test(int a = 10, int b = 20, int c = 30) {
    cout << a + b + c<< endl;
}
// 形参b设置默认值，那么后面的形参c也需要设置默认值，如果一个位置有个默认参数，那么后面的参数也必须有默认值
void test(int a, int b = 20, int c = 30) {}
// 如果函数声明和函数定义分开，函数声明设置了默认参数，函数定义不能在设置默认参数
void test(int a = 0, int b = 0); // 声明时
void test(int a, int b) { //定义时
	// ...
}
```

### 占位参数

```cpp
void test(int a, int = 1) {}
```

​		占位参数，函数调用时必需提供这个参数，但是用不到参数，可以有默认值

## 函数重载

实现重载的条件

- 同一个作用域
- 参数个数不同
- 参数类型不同
- 参数顺序不同

当函数重载碰到默认参数时，要注意避免二义性问题

```cpp
void func2(int a, int b = 10) {}
void func2(int a){}
这里出现了二义性问题
```

引用的重载

```cpp
void func(int &a) {} //引用必需要合法的空间
void func(const int &a) {} //const 也可以作为重载的条件

void test() {
    func(10);
}
```

### 函数重载的原理

​		编译器为了实现重载，会用不同的参数来修饰不同的函数名，比如`void func();` 编译器可能会将函数名修饰成`_func`，当编译器碰到`void func(int x);`编译器可能会将函数名修饰为`_func_int`，当编译器遇到`void func(int x, char c);`编译器可能会将函数名修改为`_func_int_char`。这个可能字眼是因为不同的编译器有不同的规则

### `extern C`

在`C++`中函数可以重载，在编译器会将函数名称偷偷改变，但是如果想调用`C`语言的方法时，也会将函数名改变，但是`C`中是没有重载的，所以编译会出错。这时使用`extern`可以将函数以`C`语言方式做链接。

```cpp
extern "C" void show();
```

也可以在`C`的头文件中加上

```cpp
#ifdef __cplusplus
extern "C"{
#endif
void show();
#ifdef __cplusplus
}
#endif
```

## 封装

​		封装就是将现实中的具体的事物抽象化，把其具有的属性和操作合成一个整体，封装到一个类中。

​		`C`语言使用`struct`来进行封装，但是在`C`语言中的`struct`不能写成员函数，属性和行为是分离的，类型检测不够，写起来比较麻烦。

​		`C++` 中的封装，严格类型转换检测，让属性和行为绑定到一起。属性和行为作为一个整体来表示生活中的事物。`C++`中控制权限 `public`公共权限、`private`私有权限、`protect`保护权限。

​		在`C++`中`struct`和`class`是一个意思，唯一的不同是默认权限，`struct`是`public`，但是`class`的默认权限是`private`。

```cpp
class Animal{
    void eat();
    // 如果不声明权限，默认权限是private
    //所谓私有权限就是私有成员（属性、函数），在类内部可以访问，类外部不可以访问
    public：
        int height;
    // 公共权限，在类内部和类外部都可以访问
    protected:
    	int wight;
    // 保护权限，类内部可以访问，（当前类的子类可以访问），类外部不可以访问
}
```

|  关键词   | 类内访问 | 类外访问 | 子类访问 |
| :-------: | :------: | :------: | :------: |
| `public`  |   可以   |   可以   |   可以   |
| `protect` |   可以   |  不可以  |   可以   |
| `private` |   可以   |  不可以  |  不可以  |

### 封装一个立方体类

```cpp
class Cube{
public:
  void setL(int l) {m_L = l;}
  int getL() {return m_L;}
  void setW(int w) {m_W = w;}
  int getW() const{return m_W;} //成员函数加const，代表这个成员函数没有修改成员属性
  void setH(int h) {m_H = h;}
  int getH() {return m_H;}
  void getCubeS() {
    cout << "立方体面积为:" << 2 * m_L*m_W + 2 * m_W * m_H + 2 * m_L * m_H << endl;
  }
  void getCubeV() {
    cout << "立方体体积:" << m_L * m_W * m_H << endl;
  }
  //成员函数判断是否相等
  bool compareCubeByClass(Cube & cube) {
    //...
  }

private:
  int m_L;
  int m_W;
  int m_H;
};
// 传入参数如果加了const，那么只能调用const方法
bool compareCube(Cube & cub1, Cube & cub2) {
  // ...
}
```

## 对象的构造和析构

构造函数没有返回值，没有void，类名相同，可以发生重载，可以有参数

析构函数写法，与类名相同，类名前面加上一个符号 ~ ,也没有返回值，不写void，不可以有参数（不能发生重载）

```cpp
class Person {
public:
// 构造函数写法，与类名相同，没有返回值，可以发生重载（可以有参数）
// 构造函数由编译器自动调用，而不是手动，而且只会调用一次
  Person() {
    cout << "构造函数" << endl;
  }
// 析构函数写法，与类名相同，类名前面加上一个符号 ~ ,也没有返回值，不写void，不可以有参数（不能发生重载）
// 自动调用，只会调用一次
  ~Person(){
    cout << "析构函数" << endl;
  }
};

void test() {
  Person p1;
  //默认调用构造和析构，是系统提供的两个空函数
}

```

### 构造函数的分类及调用

**按照参数进行分类** 分为无参构造函数，有参构造函数

**按照类型进行分类** 分为普通构造函数，拷贝构造函数

**无参构造写法和调用** 

- `Person p1;` 注意不能写成`Person p1()`, 因为编译器认为这个是函数声明

**有参构造写法和调用** 

- `Person p2(10)或者 Person p2 = Person(10)`
- `Person(10)`匿名对象，执行当前行后就会释放这个对象

**拷贝构造函数**

- `Person(const Person &p)`
- `Person p1(p2)` 或者 `Person p1 = Person(p2)`
- 不能用拷贝构造函数初始化匿名对象
  - 如果写成 `Person (p1)` 这种写法等价于 `Person p1`
  - 写到右值可以做拷贝构造函数

- `Person p = 100` ,隐式类型转换，相当于调用 `Person=Person(100)`

```cpp
class Person {
public: // 构造和析构必须写在public下
  Person() { // 默认 无参构造函数
    cout << "构造";
  }
  Person(int a) { //有参构造函数 
    cout << a << endl;
  }
  Person(const Person& p) { // 拷贝函数
    cout << "拷贝函数" << endl;
  }
  ~Person() {
    cout << "析构函数调用" << endl;
  }
};

int main() {
  Person p3; //默认构造函数不加(),加（），编译器认为这是函数的声明
  Person(100); // 叫匿名对象，匿名对象特定，如果编译器发现了对象是匿名对象，那么这行执行完，就执行析构函数
  Person p1 = Person(100); // 这时声明了一个匿名对象并将其命名为p1
  Person(p1); // 不能用拷贝构造来初始化匿名对象
  Person p4 = Person(p3); //如果写成左值，编译器认为你写Person p4,对象的声明，如果写成右值，那么可以
  Person p6 = 100; //相当于调用了Person p7 = Person(100)， 隐式类型转换
  return 0;
}
```

### 拷贝构造调用的时机

- 用已经创建好的对象来初始化新的对象

- 以值传递的方式给函数参数传值

  ```cpp
  void dowork(Person p1) {}// Person p1 = Person(p)
  ```

- 以值的方式返回局部对象

  ```cpp
  void dowork2() {
      Person p1;
      return p1;
  }
  void test() {
      Person p = dowork2();
  }
  ```

### 构造函数调用规则

系统默认给一个类提供3个函数，默认构造、拷贝构造、析构函数

- 当提供了有参构造函数，那么系统就不会给我们提供默认构造函数，但是系统还会提供默认拷贝构造函数
- 当我们提供了 拷贝构造，那么系统就不会提供其他构造了

### 深拷贝和浅拷贝

类在进行指针类型的拷贝时，浅拷贝只是简单的复制堆区地址，会导致重复释放内存的异常，而深拷贝是重新开辟一片内存空间。

```` cpp
Person(const Person &p) {
    m_age = p.m_age;
    m_name = (char*)malloc(strlen(p.m_name)+1);
    strcpy(n_name, p.m_name)
}
//析构函数
~Person(){
    if(m_name != NULL) {
        free(m_name);
        m_name = NULL;
    }
}
````

### 初始化列表

构造函数后面 +: 属性(参数),属性(参数)  ...

```cpp
//利用初始化列表初始化数据
Person(int a,int  b,int c): m_a(a), m_b(b), m_c(c) {}
```

###  类对象作为成员

构造时，类中的类成员先执行构造函数，类自身在执行构造。析构相反

### `explicit`

防止隐式类型转换

## `new` 和`delete`

- `new`在堆区开辟空间
- 所有`new`出来的对象，都会返回该类型的指针，`malloc`返回`void *`使用时需要强转
- `malloc`不会调用构造函数，`new`会调用
- `new`是运算符，`malloc`是系统的一个函数
- `delete`也是运算符，配合`new`使用，`malloc`与`free`配合使用
- 使用`void *`来接收`new`出来的指针，会出现释放问题
- `new`会调用默认构造函数
- `new`申请内存是无需指定内存块大小，`malloc`需要

```cpp
Person *pa = new Person[10];
delete [] pa;
// new 数组时需要有默认构造函数
// delete 数组时需要加[]
// new 的时候加[], 那么delete时加上，new的时候不加，那么delete时也不加
```

