package pol.log;

import com.google.gson.Gson;
import com.google.gson.JsonElement;

import pol.utils.JsonHelper;

/**
 * General description_________________________________________________________
 * CSV schema formatter class
 * 
 * @author Joon-Seok Kim (jkim258 at gmu.edu)
 * 
 */
public class GsonCsvSchemaFormatter extends GsonFormatter {
	private static final long serialVersionUID = 2623016863542230644L;

	public GsonCsvSchemaFormatter(Gson gson) {
		super(gson);
	}

	protected String format(Object value) {
		JsonElement element = getGson().toJsonTree(value);
		return JsonHelper.getSchema(element);
	}
}
