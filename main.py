from application.webservice.api.server import launch

if __name__=="__main__":
    app=launch()
    app.run(host="0.0.0.0", port=5000,debug=True)

