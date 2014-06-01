import webapp2
import cgi

def escape_html(s):
    return cgi.escape(s, quote = True)

form = """
<form method="post">
    <h1>ROT13</h1>
    <h2>enter your text here<h2>
    <br>
    <label>
        <textarea rows="20" cols="100" name="text">%(text)s</textarea>
    </label>
    
    <!--<div style="color: red">%(text)s</div>--!>
    <br><br>
    <input type="submit">
</form>
"""


def rot13(text):
    a="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b=""
    c="!@#$%^&*(){}[]'<>,.?/-+"
    i=0
    while(i<(len(text))):
        
        for l in range(len(a)):
            if(text[i]==a[l]):
                k=l
                if((k<25 and (k+13)<26) or (k>25 and (k+13)<52)):
                    b+=a[l+13]
                elif(k<26 and (k+13)>25):
                    v=k+13
                    b+=a[v-26]
                elif(k>25 and (k+13)>51):
                    v=(k+13)-52
                    b+=a[26+v]
            elif(text[i]==" "):
                b+=" "
                break
            elif(l<len(c) and text[i]==c[l]):
                b+=c[l]
                break
            

        i=i+1
    return b

class MainPage(webapp2.RequestHandler):
    def write_form(self, text=""):
        self.response.out.write(form %{"text": escape_html(rot13(text))})
                                       

    def get(self):
        self.write_form()
        #self.response.out.write(form)

    def post(self):
        user_text = self.request.get('text')
        self.write_form(user_text)


application = webapp2.WSGIApplication([('/', MainPage),
                              ],
                             debug=True)