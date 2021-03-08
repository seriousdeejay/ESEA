const API_URL = 'http://127.0.0.1:8000' // process.env.baseURL || process.env.apiUrl ||
const STATUS = {
    IDLE: 'idle',
    IN_PROGRESS: 'in progress',
    LOADING: 'Loading',
    ERROR: 'Error',
    SUCCESS: 'Succes'
}
const QUESTION_TYPES = {
    TEXT: 'TEXT',
	NUMBER: 'NUMBER',
	RADIO: 'RADIO',
	CHECKBOX: 'CHECKBOX'
}

export { STATUS, API_URL, QUESTION_TYPES }
