import React from 'react';
import ReactDOM from 'react-dom';
import _ from 'lodash';
import SocketIoHelper from './helpers/socketIoHelper';

class Hello extends React.Component {
	componentDidMount() {
		SocketIoHelper.setup();
	}

	render() {
    	return <div>
    		<h3>Distance: {_.get(this.props, 'sensors.distance')}</h3>
    		<h3>Temperature: {_.get(this.props, 'sensors.temperature')}</h3>
    	</div>
  	}
}

ReactDOM.render(<Hello sensors = {window.props}/>, document.getElementById('hello'));