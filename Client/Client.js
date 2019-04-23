const Ice = require("ice").Ice;
const AppServer = require("./MP3Manager").AppServer;

(async function() {
    let communicator;
    let id = 0;
    let menu = true;
    try {
        communicator = Ice.initialize();
        const base = communicator.stringToProxy("SimpleMP3Manager:default -p 10000");
        const mp3Manager = await AppServer.MP3ManagerPrx.checkedCast(base);
        if (mp3Manager) {
            while (menu) {
                console.log("Veuillez sélectionner une option : ");
                console.log("1. Ajouter une musique");
                console.log("2. Supprimer une musique");
                console.log("3. Jouer une musique (pas encore implémentée...)");
                console.log("4. Rechercher une musique");
                console.log("5. Afficher toutes les musiques\n");
                console.log("Saisissez 'q' pour quitter le programme\n");

                var choice = await getline();
                if (choice == "1") {
                    console.log("Saisissez le titre de la piste :");
                    var title = await getline();
                    console.log("Saisissez le nom de l'artiste :");
                    var artist = await getline();
                    console.log("Saisissez le titre de l'album :");
                    var album = await getline();
                    console.log("Saisissez le chemin de la musique :");
                    var path = await getline();

                    let track = new AppServer.Track(id, title, artist, album, path);
                    if(await mp3Manager.add(track)) {
                        console.log(
                            "\nLa musique " +
                                track.title +
                                " de " +
                                track.artist +
                                " a été ajouté à la base de données.\n");
                    }
                    id++;
                } else if (choice == "2") {
                    console.log("Saisissez le titre de la musique à supprimer :");
                    var title = await getline();
                    let track = await mp3Manager.search("title", title)
                    if(track) {
                        if(await mp3Manager.remove(track.title))
                            console.log("\nLa musique " + track.title + " a été supprimé de la base de données.\n");
                    }
                    else console.log("\nLa musique correspondante au titre " + title + " n'a pas été retrouvée dans la base de données...\n");
                } else if (choice == "3") {
                    console.log("\nCette fonction n'est pas encore implémentée...\n");
                } else if (choice == "4") {
                    console.log("Saisissez le type de ce que vous souhaitez rechercher (titre, artiste, album) :");
                    let track = null;
                    var searchType = await getline();
                    switch(searchType) {
                        case "titre":
                            console.log("Saisissez le titre à rechercher :");
                            var title = await getline();
                            title.toLowerCase;
                            track = await mp3Manager.search("title", title);
                            
                            break;
                        case "artiste":
                            console.log("Saisissez l'artiste à rechercher :");
                            var artist = await getline();
                            artist.toLowerCase();
                            track = await mp3Manager.search("artist", artist);
                            break;
                        case "album":
                            console.log("Saisissez l'album à rechercher :");
                            var album = await getline();
                            album.toLowerCase();
                            track = await mp3Manager.search("album", album);
                            break;
                        default:
                            console.log("Le type saisi ne correspond à aucun type prédéfini (titre, artiste, album).");
                    }
                    if(track)
                        console.log("\n--- " + track.title + " ---\n" + track.artist + " - " + track.album + "\n");
                    else console.log("\nAucune musique correspondant à votre recherche n'a été trouvé dans la base de données...\n");
                    
                } else if (choice == "5") {
                    let trackList = await mp3Manager.getTrackList();
                    console.log(trackList);
                    
                }
                else if (choice == "q") {
                    menu = false;
                }
            }
        } else {
            console.log("Invalid proxy");
        }
    } catch (ex) {
        console.log(ex.toString());
        process.exitCode = 1;
    } finally {
        if (communicator) {
            await communicator.destroy();
        }
    }
})();

function getline() {
    return new Promise(resolve => {
        process.stdin.resume();
        process.stdin.once("data", buffer => {
            process.stdin.pause();
            resolve(buffer.toString("utf-8").trim());
        });
    });
}
