/*
   Project:       videoCapture
   File Name:     play
   Author:        Chaos
   Email:         life0531@foxmail.com
   Date:          2021/4/28
   Software:      PyCharm
*/

var video = document.getElementById("input_video")
video.onended = function(){
    alert("播放完成");
}