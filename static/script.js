$(document).ready(function () {
    const topArtistsList = $('#topArtists');
    const recommendedTracksList = $('#recommendedTracks');

    function displayTopArtists(artists) {
        topArtistsList.empty().append(artists.map((artist, index) => `<li>${index + 1}. ${artist}</li>`));
    }

    function displayRecommendedTracks(recs) {
        recommendedTracksList.empty().append(recs.map((track, index) => {
            const artists = track.artists.join(', ');
            return `<li>${index + 1}. ${track.name} - ${artists}</li>`;
        }));
    }

    $.getJSON('/get_top_artists_and_recommendations', function (data) {
        displayTopArtists(data.artists);
        displayRecommendedTracks(data.recommendations);
    });
});