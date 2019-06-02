let city = ['Hanoi', 'Mexico', 'New York', 'Hong Kong'];
city.push('LA');
city.forEach(hello => {
    console.log('welcome to', `${hello}`);
});

let times = 0;
do {
    times++;
    console.log('kill yourself');
} while (times < 10);
for (i in city) {
    if (city[i].length >= 6) {
        console.log(city[i], ' is a long named city');
    };
};