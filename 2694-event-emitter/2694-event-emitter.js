class EventEmitter {
    mappedCbs = {};
    /**
     * @param {string} eventName
     * @param {Function} callback
     * @return {Object}
     */
    subscribe(eventName, callback) {
        if (!this.mappedCbs.hasOwnProperty(eventName)){
            this.mappedCbs[eventName] = new Set();
        }
        this.mappedCbs[eventName].add(callback);
        
        return {
            unsubscribe: () => {
                this.mappedCbs[eventName].delete(callback);
            }
        };
    }
    
    /**
     * @param {string} eventName
     * @param {Array} args
     * @return {Array}
     */
    emit(eventName, args = []) {
        const res = [];
        (this.mappedCbs[eventName] ?? []).forEach((fn) => {
            const val = fn(...args);
            res.push(val);
        })
        return res;
    }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */