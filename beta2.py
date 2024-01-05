from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    passo1 = request.form['passo1']
    if passo1 == "Sim":
        resultado = "Vá treinar em jejum"
    elif passo1 == "Não":
        passo2 = request.form['passo2']
        if passo2 == "8h":
            resultado = "Tome café da manhã!"
        else:
            resultado = "Horário desconhecido!"
    else:
        resultado = "Resposta inválida!"
    return render_template('resultado.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
