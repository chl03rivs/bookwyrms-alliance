// Retro submit button
// Adapted from: https://codepen.io/b1tn3r/pen/YjOzRv

// Button Hover and Active Effects
document.querySelectorAll('.btn').forEach(button => {
    // Click
    button.addEventListener('mousedown', () => button.classList.add('btn-active'));
    button.addEventListener('mouseup', () => button.classList.remove('btn-active'));
    // Hover
    button.addEventListener('mouseleave', () => button.classList.remove('btn-center', 'btn-right', 'btn-left', 'btn-active'));
    button.addEventListener('mousemove', e => {
        const { left: leftOffset, width: btnWidth } = button.getBoundingClientRect();
        const myPosX = e.pageX;
        const newClass = myPosX < leftOffset + 0.3 * btnWidth
            ? 'btn-left'
            : myPosX > leftOffset + 0.65 * btnWidth
                ? 'btn-right'
                : 'btn-center';
        // Remove previous hover classes and add the new one
        button.className = button.className.replace(/btn-center|btn-right|btn-left/g, '').trim() + ' ' + newClass;
    });
});
// Handles the loader button
class LoaderButton {
    constructor(button, options = {}) {
        this.button = button;
        this.options = Object.assign({ statusTime: 1500 }, options);
        this._init();
    }
    _init() {
        this._create();
        this._initEvents();
    }
    _create() {
        /*Dynamically builds the HTML structure needed for the loader animation and injects it into the button*/
        const textEl = document.createElement('span');
        textEl.className = 'content';
        textEl.innerHTML = this.button.innerHTML;

        const progressEl = document.createElement('span');
        progressEl.className = 'progress';

        const progressInnerEl = document.createElement('span');
        progressInnerEl.className = 'progress-inner';
        progressEl.appendChild(progressInnerEl);

        this.button.innerHTML = '';
        this.button.appendChild(textEl);
        this.button.appendChild(progressEl);

        this.progress = progressInnerEl;
        this.progressProp = 'width';
        this._enable();
    }
    _setProgress(val) {
        /*Adjusts the width of the progress bar based on the given 'val'*/
        this.progress.style[this.progressProp] = `${100 * val}%`;
    }
    _initEvents() {
        /*Sets up event listeners for button clicks to trigger the loading effect*/
        this.button.addEventListener('click', () => {
            this.button.setAttribute('disabled', '');
            this.progress.classList.remove('notransition');
            this.button.classList.add('state-loading');

            setTimeout(() => {
                if (typeof this.options.callback === 'function') {
                    this.options.callback(this);
                } else {
                    this._setProgress(1);
                    this.progress.addEventListener('transitionend', this._onTransitionEnd.bind(this));
                }
            }, 200);
        });
    }
    _onTransitionEnd(ev) {
        /*Handles the end of the transition for the loading bar*/
        if (ev.propertyName === this.progressProp) {
            this.progress.removeEventListener('transitionend', this._onTransitionEnd);
            this._stop();
        }
    }
    _stop(status) {
        /*Stops the loading animation and either displays a success or error state, or resets the button*/
        setTimeout(() => {
            this.progress.style.opacity = 0;
            this.progress.addEventListener('transitionend', ev => {
                if (ev.propertyName === 'opacity') {
                    this.progress.classList.add('notransition');
                    this.progress.style[this.progressProp] = '0%';
                    this.progress.style.opacity = 1;
                }
            });
            if (typeof status === 'number') {
                const statusClass = status >= 0 ? 'state-success' : 'state-error';
                this.button.classList.add(statusClass);

                setTimeout(() => {
                    this.button.classList.remove(statusClass);
                    this._enable();
                }, this.options.statusTime);
            } else {
                this._enable();
            }
            this.button.classList.remove('state-loading');
        }, 100);
    }
    _enable() {
        /*Re-enables the button after the loading or status effect is done*/
        this.button.removeAttribute('disabled');
    }
}

document.addEventListener('DOMContentLoaded', function() {
    // Initializes the Loader Button
    document.querySelectorAll('button.loader-button').forEach(button => {
        new LoaderButton(button, {
            callback(instance) {
                let progress = 0;
                const interval = setInterval(() => {
                    progress = Math.min(progress + Math.random() * 0.1, 1);
                    instance._setProgress(progress);

                    if (progress === 1) {
                        instance._stop(1);
                        clearInterval(interval);
                    }
                }, 200);
            }
        });
    });
});