from flask import Blueprint, render_template, request, flash, redirect, url_for
from openstackr.util import get_resource, post_resource, delete_resource

bp = Blueprint('schedules', __name__, url_prefix='/schedules')


@bp.route('/', methods=['GET', 'POST'])
def index():
    schedules = get_resource('schedules')
    images = get_resource('images')
    flavors = get_resource('flavors')
    networks = get_resource('networks')

    if request.method == 'POST':
        peak_start = request.form['peak_start']
        peak_end = request.form['peak_end']
        image = request.form['image']
        flavor = request.form['flavor']
        network = request.form['network']
        count = request.form['count']

        if not peak_start:
            flash('Please enter the peak start', 'error')
            return render_template('schedules/index.html',
                                   schedules=schedules, images=images, flavors=flavors, networks=networks)

        if not peak_end:
            flash('Please enter the peak end', 'error')
            return render_template('schedules/index.html',
                                   schedules=schedules, images=images, flavors=flavors, networks=networks)

        if not image:
            flash('Please select an image', 'error')
            return render_template('schedules/index.html',
                                   schedules=schedules, images=images, flavors=flavors, networks=networks)

        if not flavor:
            flash('Please select a flavor', 'error')
            return render_template('schedules/index.html',
                                   schedules=schedules, images=images, flavors=flavors, networks=networks)

        if not network:
            flash('Please select a network', 'error')
            return render_template('schedules/index.html',
                                   schedules=schedules, images=images, flavors=flavors, networks=networks)

        if not count:
            flash('Please enter the number of instances to run during the peak', 'error')
            return render_template('schedules/index.html',
                                   schedules=schedules, images=images, flavors=flavors, networks=networks)

        try:
            count = int(count)
        except ValueError:
            flash('Count must be a digit', 'error')
            return render_template('schedules/index.html',
                                   schedules=schedules, images=images, flavors=flavors, networks=networks)

        data = {
            'peak_interval': {
                'start': peak_start,
                'end': peak_end
            },
            'server': {
                'image': image,
                'flavor': flavor,
                'network': network,
                'count': count
            }
        }

        schedule = post_resource('schedules', data)

        if schedule is None:
            flash('Something went wrong. Please try later.', 'error')
        else:
            flash('Schedule successfully created: {}'.format(schedule), 'success')
            return redirect(url_for('schedules.index'))

    return render_template('schedules/index.html',
                           schedules=schedules, images=images, flavors=flavors, networks=networks)


@bp.route('/<string:scheduleId>')
def delete(scheduleId):
    if delete_resource('schedules', scheduleId):
        flash('Schedule {} successfully removed', 'success')
    else:
        flash('Something went wrong. Please try later.', 'error')

    return redirect(url_for('schedules.index'))
