from flask import Flask, render_template
import requests
from flask import request

app = Flask(__name__)


@app.route('/')
def home_page():
    with open('static/focus/focus.txt', 'r') as file:
        content = file.read().split('\n')
        focus = eval(content[0])
        time = eval(content[1])
        # eval()字符串转列表

    focus = focus
    time = time
    print(focus)
    print(time)

    return render_template('index.html', focus=focus,time=time)

@app.route('/getData', methods=['GET', 'POST'])
def getData():
    data = request.form['focus_list']
    time = request.form['time_list']
    with open('static/focus/focus.txt', 'w') as file:
        file.writelines(str(data))
        file.writelines(str(time))

    return request.form

@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/generic')
def generic():
    # response = requests.get('http://60.205.250.106:5000/search?key='+'动态规划例题') 
    # print(response.json())  
    print(requests)
    print(request.args.get('weak_knowledage'))
    weak_knowledage = request.args.get('weak_knowledage')
    weak_knowledage = weak_knowledage.split(',')
    print(weak_knowledage)
    data_imp = []
    for i in range(len(weak_knowledage)):
        response = requests.get('http://60.205.250.106:5000/search?key='+weak_knowledage[i]) 
        print(i)
        data_imp.append(response.json())   
        print(response.json())  
        # data = response.json()
        # data_imp = data
       
    print('hhh')
    print(data_imp)
    print(1)
    print("1",data_imp[0])
    print(2)
    print("2",data_imp[0]['data'])
    print(3)
    print("3",data_imp[0]['data'][0]['name'])
    return render_template('generic.html', data_imp=data_imp,weak_knowledage=weak_knowledage)

if __name__ == '__main__':
    app.run()
