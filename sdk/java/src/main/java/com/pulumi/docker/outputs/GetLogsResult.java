// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.docker.outputs;

import com.pulumi.core.annotations.CustomType;
import java.lang.Boolean;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class GetLogsResult {
    private @Nullable Boolean details;
    /**
     * @return Discard headers that docker appends to each log entry
     * 
     */
    private @Nullable Boolean discardHeaders;
    private @Nullable Boolean follow;
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    private String id;
    /**
     * @return If true populate computed value `logs_list_string`
     * 
     */
    private @Nullable Boolean logsListStringEnabled;
    /**
     * @return List of container logs, each element is a line.
     * 
     */
    private List<String> logsListStrings;
    /**
     * @return The name of the Docker Container
     * 
     */
    private String name;
    private @Nullable Boolean showStderr;
    private @Nullable Boolean showStdout;
    private @Nullable String since;
    private @Nullable String tail;
    private @Nullable Boolean timestamps;
    private @Nullable String until;

    private GetLogsResult() {}
    public Optional<Boolean> details() {
        return Optional.ofNullable(this.details);
    }
    /**
     * @return Discard headers that docker appends to each log entry
     * 
     */
    public Optional<Boolean> discardHeaders() {
        return Optional.ofNullable(this.discardHeaders);
    }
    public Optional<Boolean> follow() {
        return Optional.ofNullable(this.follow);
    }
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    public String id() {
        return this.id;
    }
    /**
     * @return If true populate computed value `logs_list_string`
     * 
     */
    public Optional<Boolean> logsListStringEnabled() {
        return Optional.ofNullable(this.logsListStringEnabled);
    }
    /**
     * @return List of container logs, each element is a line.
     * 
     */
    public List<String> logsListStrings() {
        return this.logsListStrings;
    }
    /**
     * @return The name of the Docker Container
     * 
     */
    public String name() {
        return this.name;
    }
    public Optional<Boolean> showStderr() {
        return Optional.ofNullable(this.showStderr);
    }
    public Optional<Boolean> showStdout() {
        return Optional.ofNullable(this.showStdout);
    }
    public Optional<String> since() {
        return Optional.ofNullable(this.since);
    }
    public Optional<String> tail() {
        return Optional.ofNullable(this.tail);
    }
    public Optional<Boolean> timestamps() {
        return Optional.ofNullable(this.timestamps);
    }
    public Optional<String> until() {
        return Optional.ofNullable(this.until);
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetLogsResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private @Nullable Boolean details;
        private @Nullable Boolean discardHeaders;
        private @Nullable Boolean follow;
        private String id;
        private @Nullable Boolean logsListStringEnabled;
        private List<String> logsListStrings;
        private String name;
        private @Nullable Boolean showStderr;
        private @Nullable Boolean showStdout;
        private @Nullable String since;
        private @Nullable String tail;
        private @Nullable Boolean timestamps;
        private @Nullable String until;
        public Builder() {}
        public Builder(GetLogsResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.details = defaults.details;
    	      this.discardHeaders = defaults.discardHeaders;
    	      this.follow = defaults.follow;
    	      this.id = defaults.id;
    	      this.logsListStringEnabled = defaults.logsListStringEnabled;
    	      this.logsListStrings = defaults.logsListStrings;
    	      this.name = defaults.name;
    	      this.showStderr = defaults.showStderr;
    	      this.showStdout = defaults.showStdout;
    	      this.since = defaults.since;
    	      this.tail = defaults.tail;
    	      this.timestamps = defaults.timestamps;
    	      this.until = defaults.until;
        }

        @CustomType.Setter
        public Builder details(@Nullable Boolean details) {
            this.details = details;
            return this;
        }
        @CustomType.Setter
        public Builder discardHeaders(@Nullable Boolean discardHeaders) {
            this.discardHeaders = discardHeaders;
            return this;
        }
        @CustomType.Setter
        public Builder follow(@Nullable Boolean follow) {
            this.follow = follow;
            return this;
        }
        @CustomType.Setter
        public Builder id(String id) {
            this.id = Objects.requireNonNull(id);
            return this;
        }
        @CustomType.Setter
        public Builder logsListStringEnabled(@Nullable Boolean logsListStringEnabled) {
            this.logsListStringEnabled = logsListStringEnabled;
            return this;
        }
        @CustomType.Setter
        public Builder logsListStrings(List<String> logsListStrings) {
            this.logsListStrings = Objects.requireNonNull(logsListStrings);
            return this;
        }
        public Builder logsListStrings(String... logsListStrings) {
            return logsListStrings(List.of(logsListStrings));
        }
        @CustomType.Setter
        public Builder name(String name) {
            this.name = Objects.requireNonNull(name);
            return this;
        }
        @CustomType.Setter
        public Builder showStderr(@Nullable Boolean showStderr) {
            this.showStderr = showStderr;
            return this;
        }
        @CustomType.Setter
        public Builder showStdout(@Nullable Boolean showStdout) {
            this.showStdout = showStdout;
            return this;
        }
        @CustomType.Setter
        public Builder since(@Nullable String since) {
            this.since = since;
            return this;
        }
        @CustomType.Setter
        public Builder tail(@Nullable String tail) {
            this.tail = tail;
            return this;
        }
        @CustomType.Setter
        public Builder timestamps(@Nullable Boolean timestamps) {
            this.timestamps = timestamps;
            return this;
        }
        @CustomType.Setter
        public Builder until(@Nullable String until) {
            this.until = until;
            return this;
        }
        public GetLogsResult build() {
            final var o = new GetLogsResult();
            o.details = details;
            o.discardHeaders = discardHeaders;
            o.follow = follow;
            o.id = id;
            o.logsListStringEnabled = logsListStringEnabled;
            o.logsListStrings = logsListStrings;
            o.name = name;
            o.showStderr = showStderr;
            o.showStdout = showStdout;
            o.since = since;
            o.tail = tail;
            o.timestamps = timestamps;
            o.until = until;
            return o;
        }
    }
}