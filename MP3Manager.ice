module AppServer { // Interface slice partagée par le client et le serveur
    class Track {
        string id;
        string title;
        string artist;
        string album;
        string path;
    };
    interface MP3Manager {
        bool add(Track track);
        bool remove(string title);
        bool play(Track track);
        Track search(string key, string value);
        string getTrackList();
    };
};