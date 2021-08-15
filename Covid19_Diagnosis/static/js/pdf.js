window.onload=function(){
   document.getElementById("download").addEventListener(
       "click",()=>{
           const page =this.document.getElementById("wholepage");
           var opt = {
               
               filename: 'report.pdf'
               
               
               };
           html2pdf().from(wholepage).set(opt).save();
       })
}