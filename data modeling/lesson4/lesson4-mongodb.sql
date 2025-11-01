db.createCollection("players");


db.players.insertMany([
  {
    player_id: 1,
    name: "Lionel Messi",
    age: 38,
    nationality: "Argentina",
    position: "Striker",
    club: "Inter Miami",
    stats: {
      matches: 25,
      goals: 18,
      assists: 12
    }
  },
  {
    player_id: 2,
    name: "Kilian Mbappe",
    age: 26,
    nationality: "France",
    position: "Midfilder",
    club: "Real Madrid",
    stats: {
      matches: 30,
      goals: 22,
      assists: 8
    }
  }
  ]);

db.players.find({ position: "Striker" });

db.players.find().sort({ "stats.goals": -1 });

