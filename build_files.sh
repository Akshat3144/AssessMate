{
    "version": 2,
    "builds" : [
        {
            "src":"myproject/wsgi.py",
            "use":"@vercel/python",
            "config":{"maxLamdaSize":"15mb","runtime":"python3.9"}
        },
        {
            "src":"build_files.sh",
            "use":"@vercel/static-build",
            "config":{
                "distDir":"staticfiles_build"
            }
        }
    ],
    "routes":[
        {
            "src":"/static/(.*)",
            "dest":"/static/$1"
        },
        {
            "src":"/(.*)",
            "dest":"myproject/wsgi.py"
        }
    ]
}
