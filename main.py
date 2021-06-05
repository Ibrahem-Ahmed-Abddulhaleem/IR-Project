from flask import Flask
from flask import render_template, request
import ir_lib
import cos_sim
app = Flask(__name__)

# def main():
#     pass

@app.route('/')
def home():
    return """
        <!DOCTYPE html>
<html>
<head>
<title>IR Project!</title>
<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
  border: 1px solid black;
}

td, th {
  text-align: left;
  padding: 8px;
  border: 1px solid black;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
</head>
<body>
<!-- Starting My code here :D -->

<h1>Inner Product</h1>
  <form action="/handle_submit_assignment1" method="POST">

    
    <input type="text" name="textfield_assignment1"/>
    <input type="submit" value="Click" />
  </form>

  <br>
  <br>
<!--
<h1>Similarity</h1>
    <form action="/handle_submit_assignment2" method="POST">

    
    <input type="text" name="textfield_assignment2"/>
    <input type="submit" value="Click" />
  </form>

-->

  <h1>Cosine Similarity</h1>
    <form action="/handle_submit_assignment3" method="POST">

    
    <input type="text" name="textfield_assignment3"/>
    <input type="submit" value="Click" />
  </form>

<!-- End My code here -->
</body>
</html>
    
    """


@app.route("/handle_submit_assignment1", methods=["POST"])
def handle_submit_assignment1():
    user_query = request.form["textfield_assignment1"].upper()
    result = ir_lib.calculate(user_query)
    output = "<table><tr><th>SIM</th><th>File</th></tr>"
    for key in result:
          output+="<tr>"
          output+="<td>"
          output+=str(key[0])
          output+="</td>"

          output+="<td>"
          output+=key[1]
          output+="</td>"

          output+="</tr>"

    output+="</table>"
    return output

@app.route("/handle_submit_assignment2", methods=["POST"])
def handle_submit_assignment2():
    user_query = request.form["textfield_assignment2"].upper()
    # result = ir_lib.calculate(user_query)
    # print(user_query)
    result = cos_sim.calculate(user_query)

    output = "<table><tr><th>SIM</th><th>File</th></tr>"
    for key in result:
          output+="<tr>"
          output+="<td>"
          output+=str(key[0])
          output+="</td>"

          output+="<td>"
          output+=key[1]
          output+="</td>"

          output+="</tr>"

    output+="</table>"
    return output


@app.route("/handle_submit_assignment3", methods=["POST"])
def handle_submit_assignment3():
    user_query = request.form["textfield_assignment3"].upper()
    # result = ir_lib.calculate(user_query)
    # print(user_query)
    result = cos_sim.calculate_cos_sim(user_query)
    print(result)
    output = "<table><tr><th>COS SIM</th><th>File</th></tr>"
    for key in result:
          output+="<tr>"
          output+="<td>"
          output+=str(key[0])
          output+="</td>"

          output+="<td>"
          output+=key[1]
          output+="</td>"

          output+="</tr>"

    output+="</table>"
    return output

if __name__ == '__main__':
    # main()
    app.run(debug=True)
    
    