# [WORK ISSUE](https://github.com/linziyang1106/2022/issues/2)

工作遇到的问题

---

## 文件预览问题
两种情况
1. 打开链接，不在页面上显示文件，直接下载
2. 打开链接，在页面上显示文件，不直接下载文件

response header
`"Content-Disposition","attachment;filename=FileName.txt")`
<img width="261" alt="image" src="https://user-images.githubusercontent.com/54968314/148341226-55e8ac9e-d5ba-4cbe-89cc-143ef1703a39.png">

### 原因
由`Content-Disposition`和`Content-Type`这两个参数决定
当`Content-Disposition`为 `attachment`时，表示告诉浏览器这是要下载的文件
要在网页上直接预览的话徐修改为`inline`

当`Content-Type`为 `application/form-data`的时候，也是会直接下载文件
要在页面上预览的话必须要使用对应的文件格式，如
+ pdf    ---- `Content-Type: application/pdf`
+ 图片  ---- `Content-Type: image/png` 或者 `Content-Type: image/jpg`


---

## 文件和目录同名问题

建议

1. 一般目录都不能同名
2. 当上传文件同名时，应该让用户选择是否替换还是同时保留，如果同时保留则将文件名后缀加标识符
3. 不同目录下的文件名可以相同（目录也是类似）

### AliyunDrive

个人认为阿里云盘做的还是比较人性化 也比较好看

<img width="446" alt="image" src="https://user-images.githubusercontent.com/54968314/148484058-54bb59e2-f6c3-4f7f-9f91-f17cce353cf6.png">
<img width="495" alt="image" src="https://user-images.githubusercontent.com/54968314/148484138-07fa37fc-e601-4481-8e18-9519c2812898.png">
