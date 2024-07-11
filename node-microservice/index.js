const express = require('express');
const mysql = require('mysql2');
const axios = require('axios');


const app = express();
const port = 3000;
const cors = require('cors');

const DBConnection = mysql.createConnection(
    {
        host: '127.0.0.1',
        user: 'root',
        password: 'avsha1401',
        database: 'entrio_db',
    }
)


app.use(cors());


app.get(
    '/api/get_all_repositories',
    (req, res) => {
        console.log("getting all repositories")

        const repositoriesQuery = "SELECT * FROM entrio_db.repositories;"

        DBConnection.connect(
            (err) => {
                if (err) {
                    res.status(500).send("db connection error");
                }

                else {
                    DBConnection.query(
                        repositoriesQuery,
                        (err, result, fields) => {
                            if (err) {
                                res.status(500).send("query error");
                            }

                            else {
                                const response = {
                                    data: result,
                                }
                                res.status(200).json(response)
                            }

                        }
                    )
                }
            }
        )
    }
)

app.get(
    '/api/get_repository',
    (req, res) => {
        const repositoryFirstName = req.query.repository_first_name;
        const repositoryLastName = req.query.repository_last_name
        const repositoryFullName = `${repositoryFirstName}/${repositoryLastName}`;
        const repositoryID = req.query.repository_id;

        const hasRepositoryFullName = typeof repositoryFirstName !== 'undefined' && typeof repositoryLastName !== 'undefined';
        const hasRepositoryID = typeof repositoryID !== 'undefined';

        const url = new URL(`http://127.0.0.1:8000/entrio_app/get_repository_details/${repositoryFullName}`);

        let repositoryQuery = null;

        if (hasRepositoryFullName) {
            repositoryQuery = `SELECT * FROM entrio_db.repositories WHERE NAME = '${repositoryFullName}';`;
        }

        else if (hasRepositoryID) {
            repositoryQuery = `SELECT * FROM entrio_db.repositories WHERE ID = '${repositoryID}';`;
        }

        else {
            res.status(400).send('no repository name and id');
        }

        DBConnection.connect(
            (err) => {
                if (err) {
                    res.status(500).send("db connection error");
                }

                else {
                    DBConnection.query(
                        repositoryQuery,
                        (err, result, fields) => {
                            if (err) {
                                res.status(500).send("query error");
                            }

                            else {
                                console.log(url.toString())
                                if (result.length === 0 && hasRepositoryFullName) {
                                    axios.get(
                                        url.toString(),
                                    ).then(
                                        result => {
                                            const response = {
                                                data: result.data.response.repository,
                                            }
                                            res.status(200).json(response);
                                        }
                                    ).catch(
                                        error => {
                                            res.status(500).send(error);
                                        }
                                    )
                                }

                                else if (result.length === 0 && hasRepositoryID) {
                                    res.status(400).send('id was not found in the db');
                                }

                                else {
                                    const response = {
                                        data: result[0],
                                    }
                                    res.status(200).json(response);
                                }
                            }
                        }
                    )
                }
            }
        )
    }
)

app.listen(
    port,
    () => {
        console.log(`node server on http://localhost:${port}`);
    }
)
