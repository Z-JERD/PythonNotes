
# 如何创建响应式布局？

# 你曾经使用过哪些前端框架？
'''
jquery,bootstrap,vue
jquery是JavaScript库,能够极大地简化JavaScript编程,能够更方便的处理DOM操作和进行Ajax交互
Bootstrap是基于HTML,CSS，javascript的前端框架,使用它可以快速的搭建出网站
'''
# 什么是ajax请求？并使用jQuery和XMLHttpRequest对象实现一个ajax请求
'''
在不刷新整个网页的情况下，AJAX通过后台加载数据，并在网页上进行显示

'''
# 如何在前端实现轮训？
'''
在特定的时间间隔,由浏览器对服务器发出请求,然后服务器把最新的数据返回给客户端
轮训需要更快的处理速度
'''
# 如何在前端实现长轮训？
'''
    页面在发送ajax后,服务器端会阻塞请求直到有数据传递或超时才返回。
    客户端JavaScript响应处理函数,在处理完返回的信息后，再次发出请求，重新建立连接。
    长轮询更要求更高的处理并发的能力
'''
# vuex的作用？
'''
作用:状态管理库,利用 Vue.js的数据响应机制来进行高效的状态更新
Vuex的状态存储是响应式的，当Vue组件从store中读取状态时，若store中状态发生改变，响应的组件也会得到更新状态。
但不能直接改变state,必须通过显示的提交mutations来追踪每一个状态的变化。
'''
# 列举vue的常见指令
'''
v-bind : 属性绑定
v-on : 事件绑定
v-model：在表单 <input> 及 <textarea> 元素上创建双向数据绑定
v-if,v-else : 条件渲染，进行判断
v-show : 类似判断 , 会有一个隐藏的标签
v-for：列表渲染 
v-html：输出HTML
'''
# vue中的路由的拦截器的作用？
'''
验证要跳转的url,来决定是跳转到登录页面还是留在当前页面继续获取数据
'''
# axios的作用？

# 简述jsonp及实现原理？
# 是什么cors ？
下列的值是什么
1.
'''
<script>
    var name="jerd";
    function func(){
        var name="ruby";
        function inner(){
            alert(name);
        }
        return inner;
    }
    var ret=func();
    ret();
</script>
#ruby
'''
2.
'''
<script>
    function main(){
        if(1==1){
            var name='ruby';
        }
        alert(name);
    }
     main()
</script>
#ruby
'''
3.
'''
<script>
    var name='jerd';
    function func(){
       var name="ruby";
       function inner(){
           var name='python';
           alert(this.name);
       }
       inner()
    }
     func()
</script>
#jerd
'''
4.
'''
<script>
    var name='jerd';
    function Foo(){
       this.name='ruby';
       this.func=function () {
        
           alert(this.name)
       }
    }
    var obj= new Foo();
     obj.func()
</script>
#ruby
'''
5.
'''
<script>
    var name='jerd';
    function Foo(){
       this.name='ruby';
       this.func=function () {
           (function () {
               alert(this.name)  //window
           })()
       }
    }
    var obj= new Foo();
     obj.func()
</script>
#jerd
'''


