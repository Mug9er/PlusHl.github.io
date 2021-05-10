---
title: C++学习笔记(一)
mathjax: true
categories:
  - C++ 学习
  - 基础知识
tags:
  - C++
  - 基础
abbrlink: b34cf332
date: 2021-05-02 14:54:52
---

<meta name = "referrer" content = "no-referrer" />

![](https://wx1.sinaimg.cn/mw690/0083TyOJly1gq438qcpmcj31400u01cn.jpg)

<!-- less -->

# C++ 学习笔记（一）

## 双冒号运算符

作用域运算符  `::`全局作用域

```cpp
int a = 200;
void test() {
    int a = 100;
    cout << a << endl; // 输出 100
    cout << ::a << endl; //输出200
    std::cout << "nihao"; //::前面加std则是说明cout是std作用域下的
}
```

## `namespace`的使用

`namespace`命名空间主要用于解决命名冲突

- 命名空间下可以放函数、变量、结构体、类

- 命名空间必须定义在全局作用域下
- 命名空间可以检讨命名空间
- 命名空间是开放的，可以随时往原先的命名空间添加内容
- 一个命名空间分开写会自动合并
- 命名空间可以匿名，匿名命名空间内的变量相当于`static`
- 命名空间可以起别名

## `using` 声明和`using` 编译

### `using` 声明

使用`using`声明时要避免二义性问题，

```cpp
namespace KG{
    int sunwukongId = 10;
}
void test() {
    int sumwukongId = 20;
    using KG::sunwukongId;
    // 写了using 声明后，说明以后的所有sunwukongId都是KG下的，
    // 但是编译器又有就近原则，这就造成了二义性
    cout << sunwukongId << endl;
}
```

### `using` 编译

```cpp
void test2() {
    int sunwukongId = 20;
    using namespace KG; //打开命名空间KG，可以执行
    cout << sunwukongId << endl;
}
```

## C++对C的增强

### 全局变量检测增强

```cpp
//全局变量中
int a;
int a = 10;
//在C语言中可以通过编译
//在C++中不能通过编译
```

### 函数检测增强

```cpp
// 函数 参数类型增强
int getRecS(w, h) {
    // 无返回值可以通过C编译不能通过C++编译
}
// 在C中可以通过编译
// 在C++中不可以通过编译

//参数检测增强
void test02() {
    getRecS(10, 10, 10)；
}
```

### 类型转换检测增强

```cpp
void test03() {
	char *p = malloc(sizeof(64)); //malloc返回值是void*
}
// C可以通过编译，因为C认为void*是一个万能指针，可以转换成char*，
// 而C++不行，C++ 版本须为
// char *p = (char*)malloc(sizeof(64));
```

### `struct`增强

```cpp
struct Person{
	int m_Age;
    void plusAge();
    // C中struct不能加函数，C++可以
}
void test04() {
    struct Person p1; 
    // C语言必须加上struct
}
```

### `bool`类型增强

``` cpp
// C中没有bool类型，在C++中bool类型 非0的值都是1
```

### 三目运算符增强

```cpp
void test05() {
    int a = 10;
    int b = 20;
    printf("%d\n", a > b ? a : b);
    a > b ? a : b = 100;
    // 三目运算符，C语言中返回值，C++返回的是变量
    // C语言模仿C++写法
    // *(a > b ? &a : &b) = 100
}
```

### `const`增强

```cpp
const int m_A = 10; //全局const，在C和C++中都不能修改
void test07() {
   const int m_B = 20; //C中伪常量，C++中真常量
    int *p = (int*)&m_B;
    printf("%d\n", *p);
    // 在C中const的作用仅仅是不允许修改，但是可以通过指针来修改
    // 在C++中通过指针修改的仅仅是*p, 而m_B并没有变
    // int arr[m_B] 在C中不能来定义数组，在C++中可以
}
```

- `C`语言中，`const`修饰的变量，是伪常量，编译器是会分配内存的，只要分配内存就可以更改

- `C++`中，`const`不会分配内存，在`C++`中`int *p = (int*)&m_B`的`*p`指向的是编译器临时开辟的一块内存空间

- `const`在`C`中默认是外部外部链接，在其他文件中使用`extern`可以找到变量，而在`C++`中则是默认内部链接

- `const`分配内存，取地址会分配临时内存，使用`extern`时编译器也会给`const`变量分配内存，用普通变量初始化`const`变量也会给`const`分配内存

```cpp
int a = 10;
const int b = a; //会分配内存
```

- 自定义数据类型，加`const`也会分配内存

```cpp
struct Person{
    string m_Name;
    int m_Age;
}
void test() {
    const Person p1; // 分配了内存
    Person *p = (Person*)&p1;
    p->m_Name = "abc";
    (*p).m_Age = 18;
}
```

`const`和`define`区别总结

```shell
1. const 有类型，可进行编译器类型安全检查，#define五类性，不可进行检查
2. const 有作用域，而#define 不重视作用域，默认定义处到文件结尾，如果定义在指定作用域下有效的常量，那么#define就 不能用，#define可以用undef 来结束作用周期
```

## 引用

引用是`C++`对`C`的重要扩充。在`C/C++`中指针的作用基本都是一样的，但是`C++`增加了另一种给函数传递地址的途径，这就是按引用传递，他也存在与其他一些编程语言中，并不是`C++`的发明。

- 变量名实质上是一段连续内存的别名，是一个标号（门牌号）
- 程序中通过变量来申请并命名内存空间
- 通过变量的名字可以使用存储空间

```cpp
int a = 10;
int &b = a;
b = 200;//修改b时，a也会修改
```

### 引用

```cpp
引用使用格式：type &别名=原名
```

- 引用 就是起别名，这里`a`的`b`都指向同一片地址空间，`&`写到左侧叫引用，写到右侧是取地址。
- 引用必须初始化，引用初始化后不可以修改

```cpp
void test() {
    //int &a;//编译不通过
    int  a = 10;
    int &b = a; //引用初始化后不可以修改
    int c = 20;
    b = c;//这里是把c的值赋给b，而不是b引用c，初始化后不可以修改
}
```

- 对数组建立引用

```cpp
void test() {
    int arr[10];
    for (int i = 0; i < 10; i ++)
        arr[i] = i;
    int (&parr[i])[10] =  arr;
    for (int i = 0; i < 10; i ++) {
        cout << parr[i];
    }
}
```

### 参数传递

```cpp
// 值传递，直接传递a，b的值，不更改a与b的值
void swap1(int a, int b){ 
    int tmp = a;
    a = b;
    b = tmp;
}
// 指针传递，传递a，b的指针，更改a，b的值
void swap2(int *a, int *b) { 
    int tmp = *a;
    *a = *b;
    *b = tmp;
}
//引用传递，类似传递地址，相当于int &a = a，可以通过引用改变a，b的值
void swap3(int &a, int &b) { 
    int tmp = a;
    a = b;
    b = tmp;
}
void test() {
    int a = 10, b = 20;
    swap1(a, b);
    swap2(&a, &b);
    swap3(a, b);
}

```

### 引用注意事项

- 引用必需引一块合法的内存空间

  ```cpp
  void test() {
      int &a = 10;//引用必需引一块合法的内存空间
  }
  ```

- 不要返回局部变量的引用

  ```cpp
  int &dowork() {
      int a = 10;
      return a;
  }
  int& work2() {
      static int a = 10;
      return a;
  }
  void test() {
      int &ret =  dowork(); // 局部引用已经销毁，数据不准确
  	dowork2() = 1000; 
      // 如果函数的返回值引用，那么这个函数调用可以作为左值，
      //相当于写了a=1000
  }
  
  ```

  ### 引用的本质

  ```cpp
  引用的本质在C++内部实现是一个指针常量
  ```

  ### 指针的引用

  ```cpp
  struct Person{
      int m_age;
  }
  // 通过指针给对对象分配内存
  void allocat(Person **p) {
      *p = (Person *)malloc(sizeof(Person));
      (*p)->m_age = 100;
  }
  void test01() {
      Person *p = NULL;
      allocat(&p);
  }
  // 利用指针引用开辟空间
  void allocat(Person* &p) {
      p = (Person*)malloc(sizeof(Person));
      p->m_age = 100;
  }
  void test02() {
      Person *p = NULL;
      allocat(p);
  }
  ```

### 常量引用

```cpp
void test() {
    int  &ref = 10; // 引用了不合法的内存，不可以
    const int &ref = 10;
    //加入const后，编译器处理方式为
    // int tmp = 10; const int &ref = tmp;
    // 常量引用ref可以通过指针来修改
    int *p = (int*)&ref;
    *p = 1000;
    
}
```

常量引用使用场景，通常用来修饰形参

```cpp
void showValue(const int &val) {
    //如果只是想展示内容，而不修改内容，那么就用const来修饰这个形参
}
```

483