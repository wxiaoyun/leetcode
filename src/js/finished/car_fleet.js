/**
 * @param {number} target
 * @param {number[]} position
 * @param {number[]} speed
 * @return {number}
 */
var carFleet = function (target, position, speed) {
	let fleets = [];

	for (let i = 0; i < position.length; i++) {
		fleets.push({
			position: position[i],
			speed: speed[i],
		});
	}

	// can b catch up to a?
	function can_catch_up(car_a, car_b) {
		let a_time_remaining = (target - car_a.position) / car_a.speed;
		let b_time_remaining = (target - car_b.position) / car_b.speed;
		return b_time_remaining <= a_time_remaining;
	}

	fleets.sort((a, b) => a.position - b.position);

	let fleets_count = 0;

	while (fleets.length > 1) {
		let ahead = fleets.pop();
		let behind = fleets.pop();

		if (ahead.position === behind.position) {
			fleets.push({
				...ahead,
				speed: Math.min(ahead.speed, behind.speed),
			});
			continue;
		}

		if (can_catch_up(ahead, behind)) {
			fleets.push({
				...ahead,
				speed: Math.min(ahead.speed, behind.speed),
			});
			continue;
		}

		fleets.push(behind);
		fleets_count++; // behind cannot catch up to ahead
	}

	return fleets_count + fleets.length;
};
