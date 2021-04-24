# pyquery中常用选择器

![img](https://csdnimg.cn/release/blogv2/dist/pc/img/reprint.png)

[Dunkle.T](https://blog.csdn.net/weixin_44350337) 2019-08-27 22:30:36 ![img](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes.png) 445 ![img](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect.png) 收藏 1

分类专栏： [python爬虫基础](https://blog.csdn.net/weixin_44350337/category_9185979.html) 文章标签： [python](https://www.csdn.net/tags/MtjaQg4sNDk0LWJsb2cO0O0O.html) [爬虫](https://www.csdn.net/tags/MtTaEg0sMTQ4MjYtYmxvZwO0O0OO0O0O.html) [pyquery](https://www.csdn.net/tags/MtTaEg0sMTM2NTQtYmxvZwO0O0OO0O0O.html)

版权

**一、元素选择**

| *                | $("*")                | 所有元素                              |
| ---------------- | --------------------- | ------------------------------------- |
| *element*        | $("p")                | <p> 元素                              |
| *ele1,ele2*      | $("th,td")            | <th>或<td>元素                        |
| #*id*            | $("p#lastname")       | id="lastname" 的p元素                 |
| .*class*         | $("p.intro")          | class="intro" 的p元素                 |
| .*class*.*class* | $("p.intro.demo")     | class="intro" 且 class="demo" 的p元素 |
| ele:emtpy        | $("p:empty")          | 不包含子元素的p元素                   |
| ele:parent       | $("p:parent")         | 包含子元素的p元素                     |
| ele1.has(ele2)   | $("div:has(p.intro)") | 有p子元素且子元素属性为intro的div元素 |

**二、属性选择**

| [*attr*]          | $(p"[href]")         | 有href属性的p元素            |
| ----------------- | -------------------- | ---------------------------- |
| [attr1][attr2]    | $("p[title][href]")  | 同时有title和href属性的p元素 |
| [*attr*=*value*]  | $("p[href='#']")     | href 属性等于"#"的p元素      |
| [*attr*!=*value*] | $("p[href!='#']")    | href 属性不等于"#"的p元素    |
| [*attr*$=*value*] | $("p[href$='.jpg']") | href 属性以".jpg"结尾的p元素 |
| [attr^=value]     | $("p[href^='fb']")   | href 属性以"fb"开头的p元素   |
| [attr*=value]     | $("p[href*='link']") | href 属性包含"link"的p元素   |

**三、内容选择**

| :contains(value) | $("p:contains('W3School')") | 包含指定字符串的p元素 |
| ---------------- | --------------------------- | --------------------- |
|                  |                             |                       |

**四、反向选择**

| :not() | $("div:not(:has(p))")$(p:not([href])")$("p:not(:contains('abc'))") | 不包含子元素p的div元素没有属性href的元素**不包含指定字符串的p元素** |
| ------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
|        |                                                              |                                                              |

**四、关系选择**

| ele1 ele2   | $("div li")      | 元素div的后代li元素 |
| ----------- | ---------------- | ------------------- |
| ele1 > ele2 | $("div > li")    | 元素div的li子元素   |
| :eq(index)  | $("ul li:eq(3)") | 选择第4个li元素     |
| :gt(index)  | $("ul li:gt(3)") | 选择第4个以后的元素 |
| :lt(index)  | $("ul li:lt(3)") | 选择第4个以前的元素 |

 参考：http://www.w3school.com.cn/jquery/jquery_ref_selectors.asp