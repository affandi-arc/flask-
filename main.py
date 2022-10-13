from website import create_app
#Basic Route Flask
app = create_app()

#Debugging
if __name__ == '__main__':
    app.run(debug=True)
