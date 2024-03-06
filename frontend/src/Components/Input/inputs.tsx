import { Component, FormEvent } from "react";
import "./input.css"

class Input extends Component {
    props: { campo: string, type: string, internal: string, form: (arg1: string, arg2: string) => void }
    state = { texto: '' };
    constructor(props: { campo: string, type: string, internal: string, form: (arg1: string, arg2: string) => void }) {
        super(props);
        this.props = props;
        this.state = {texto: ''};
        this.onChange = this.onChange.bind(this);
    }

    onChange(event: FormEvent) {
        this.setState({ texto: event.target.value });
        this.props.form(this.props.campo, event.target.value)
    }

    render() {
        return (
            <div className={this.props.internal + " div"}>
                <div className="divWrapWrap">
                    <label className={this.props.internal + "-span input-text"}>
                        {this.props.campo}
                    <input className="input" type={this.props.type} id={this.props.campo}
                            value={this.state.texto} onChange={this.onChange} />
                    </label>
                </div>
            </div>
        );
    }
}
export default Input;